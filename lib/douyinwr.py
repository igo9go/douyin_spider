import threading
import urllib.parse
import requests
from playwright.sync_api import sync_playwright

from . import config
import re
import os
import time
import json

config.type="playwright"
config.Yescan=True

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
js="""
    Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
    """
# 获取url响应内容的 json 数据
def on_response(response):
    try:
        if re.match(r'https://www\.douyin\.com/aweme/v1/web/aweme/post/.*?device_platform=webapp',response.url):
            body=json.loads(response.body())
            if body and "aweme_list" in body:
                for it in body["aweme_list"]:
                    info={
                        "title":it["desc"],
                        "url":it["video"]["play_addr"]["url_list"][0]
                    }
                    print(info)
                    config.downloads.append(info)
    except Exception as e:
        print(e)

  

# 在作者主页，第一次获取去前10个视频页面地址，然后通过 response 事件获取ajax的json列表
def geturlbyzuozhe(url):
    config.message.append("开始获取作者主页%s的视频地址" % url)
    if not re.match("^https?:\/\/",url):
        print("url无效:%s"%url)
        return False
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=10,
            args=['--disable-blink-features=AutomationControlled','--user-agent=%s'%user_agent,'--force-webrtc-ip-handling-policy=disable_non_proxied_udp']
        )
        context=browser.new_context()
        page = context.new_page()
        page.add_init_script(js);
        page.on('response', on_response)
        page.route("**/*.{png,jpg,jpeg}",lambda route:route.abort())
        page.route("**/*",lambda route:route.abort() if route.request.resource_type=="image" else route.continue_())
        page.goto(url)

        page.wait_for_load_state('networkidle')
        print("current_url=" + page.url)
        # 如果是视频播放页url
        if re.match(r'https://www.douyin.com/video/\d+', page.url):
            config.videourls.append(page.url)
            return
        # 循环检测是否还有新内容，滚动到底部
        pagesize=0
        while True:
            if not config.runing:
                config.message.append("已停止")
                context.close()
                browser.close()
                return
            try:
                # 关闭登录框
                page.locator(".dy-account-close").click()
            except Exception:
                pass
            #第一页获取，其他监听
            pagesize+=1
            if pagesize==1:
                hrefs = page.locator('//*[@id="root"]//ul[1]/li/a[contains(@href,"/video/")]').element_handles()
                print("hrefs-length=%s" % len(hrefs))
                for href in hrefs:
                    if not config.runing:
                        config.message.append("已停止")
                        context.close()
                        browser.close()
                        return
                    u = "https:" + href.get_attribute("href")
                    if not u in config.videourls:
                        config.videourls.append(u)
                        config.message.append("\n获取到url：%s" % u)

            if page.locator("'暂时没有更多了'").count() > 0:
                config.message.append("获取作者的视频结束了")
                break
            page.keyboard.press("End")
            time.sleep(5)
        context.close()
        browser.close()
    print("待下载列表 download lenght=%s"%len(config.downloads))


# 根据config.videourls 仅将 title和url存到 config.downloads 里
def runfun():
    if not config.runing:
        config.message.append("已停止")
        return
     
    config.message.append("\n开始从视频播放页获取信息")
    # 循环获取视频播放页的title和视频下载url
    while True:
        # 停止
        if not config.runing:
            config.message.append("已停止")
            break
        #没有链接了，暂停15s
        if len(config.videourls)>0:
            url = config.videourls.pop()
        else:
            print("没有链接了，暂停15s")
            time.sleep(10)
            continue

        src=""
        if not re.match(r'https://www.iesdouyin.com/web/api/v2/aweme',url):
            #不是视频播放地址，继续
            mts=re.match(r'https://www.douyin.com/video/(\d+)', url)
            if not mts:
                # 如果是作者地址，获取开启线程
                if re.match(r'https://www\.douyin\.com/user/[\w\-]+', url):
                    # 从作者主页获取视频链接
                    threading.Thread(target=geturlbyzuozhe, args=(url,), daemon=True).start()
                    continue
                res=requests.get(url,headers=config.headers)
                mts=re.match(r'https://www.douyin.com/video/(\d+)', res.url)
                if not mts or not mts[1]:
                    # 如果是作者地址，获取开启线程
                    if re.match(r'https://www\.douyin\.com/user/[\w\-]+', url):
                        # 从作者主页获取视频链接
                        threading.Thread(target=geturlbyzuozhe, args=(url,), daemon=True).start()
                    continue
            src="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=%s"%mts[1]
        else:
            src=url
        # https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=6856737027619114247
        try:
            print("url1="+mts[1])
            res=requests.get(src,headers=config.headers)
            body=json.loads(res.text)
            src=body['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/','/play/')
            text=body['item_list'][0]['desc']
            print({"title":text,"url":src})
            config.downloads.append({"title":text,"url":src})
        except Exception as e:
            print(e)

        
# 使用requests 下载视频
def download():
    if not os.path.exists(config.saveDir):
        os.mkdir(config.saveDir)
    while True:
        if not config.runing:
            config.message.append("已停止")
            return
        if len(config.downloads)<1:
            time.sleep(15)
            continue
        it=config.downloads.pop(0)
        mp4="%s.mp4"%re.sub(r'[ #*.?&@!$%^()|]', "", it["title"]).strip()
        mp4file=os.path.join(config.saveDir, mp4)
        if os.path.exists(mp4file):
            config.message.append("已存在:%s" % mp4file)
            continue
        try:
            config.message.append("\n开始下载视频文件:%s" % mp4file)
            rep = requests.get(it["url"], headers=config.headers)
            with open(mp4file, "wb") as  f:
                f.write(rep.content)
            config.message.append("\n下载成功:%s" % mp4file)
        except Exception as e:
            config.message.append("\n下载视频文件失败了====")
            config.downloads.append(it)
            logname=time.strftime("%Y-%m-%d", time.localtime())+".log"
            with open(os.path.join(config.logsDir,logname),"ab") as f:
                msg="\n[url]%s\n[title]%s\n[error]%s\n"%(it["url"],it["title"],e)
                f.write(msg.encode("utf-8"))
        time.sleep(5)