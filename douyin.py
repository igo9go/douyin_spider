# -*- coding:utf-8 -*-
# 抖音短视频采集
import time

import requests
from PyQt5.QtCore import Qt, QThread, pyqtSignal

from lib import douyinwr as douyin
from lib import config
import threading
import os
import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import douyinui


# 另一个线程，用来触发更新进度反馈
class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        while 1:
            print("qthread-run")
            # 发送结束信号
            if len(config.message)>0:
                # 通过自定义信号把待显示的字符串传递给槽函数
                self.trigger.emit()
            time.sleep(3)


# 更新 显示结果
def showresult():
    if len(config.message)>0:
        myUi.textel.append(config.message.pop(0))
        myUi.textel.verticalScrollBar().setValue(myUi.textel.verticalScrollBar().maximum())
    


# 提示
def toast(title, text):
    box = QMessageBox(QMessageBox.Warning, title, text)
    box.addButton("知道了", QMessageBox.YesRole)
    box.exec_()

# 检测网址是否正确
def getrighturl(ztext,vtext):
    result={"msg":"","zurl":"","vurl":""}

    if len(ztext) > 0:
        g = re.findall(r'.*?(https://v\.douyin\.com/\w+/?).*?', ztext)
        g2 = re.findall(r'.*?(https://www\.douyin\.com/user/[\w\-]+[\?/]?).*?', ztext)
        if g and len(g) > 0:
            result['zurl'] = g[0]
        elif g2 and len(g2) > 0:
            result['zurl'] = g2[0]
        else:
            result["msg"] += "作者主页url不正确，请在抖音app-右上角-分享主页-复制链接\n"
    if len(vtext) > 0:
        g = re.findall(r'.*?(https://www\.douyin\.com/video/\d+)\??.*?', vtext)
        g2 = re.findall(r'.*?(https://v\.douyin\.com/\w+/?).*?', vtext)

        if g and len(g) > 0:
            result["vurl"] = g[0]
        elif g2 and len(g2) > 0:
            result["vurl"] = g2[0]
        else:
            result["msg"] += "视频地址url不正确，请在抖音app-视频播放页-分享按钮-复制链接\n"
    if not result["zurl"] and not result["vurl"]:
        result["msg"]+="作者主页和视频地址，至少填写一个"
    return result
# 开始按钮绑定函数
def startfun(myUi):
    if not config.Yescan:
        toast("不符合执行条件","请按照下方提示配置环境")
        return
    if config.runing:
        config.runing = False
        myUi.startbtn.setText("已停止，点击重新开始")
        return False


    reslist=getrighturl(myUi.zuozheinput.text().strip(),myUi.videoinput.text().strip())
    if reslist["msg"]:
        toast("出错了", reslist["msg"])
        return False
    # 删掉错误消息
    config.runing = True
    myUi.startbtn.setText("运行中，点击停止")
    if "vurl" in reslist and len(reslist['vurl'])>5:
        config.videourls.append(reslist["vurl"])
    print(reslist)
    # return
    # 开始运行
    if "zurl" in reslist and  len(reslist['zurl'])>5:
        # 从作者主页获取视频链接
        threading.Thread(target=douyin.geturlbyzuozhe, args=(reslist["zurl"],), daemon=True).start()
    
    # 根据视频链接获取视频
    threading.Thread(target=douyin.runfun, daemon=True).start()
    
    # 下载线程 3 个
    threading.Thread(target=douyin.download, daemon=True).start()
    threading.Thread(target=douyin.download, daemon=True).start()
    threading.Thread(target=douyin.download, daemon=True).start()
    
    
    config.message.append("已开始执行，请等待...")


if __name__=="__main__":

    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = douyinui.Ui_MainWindow(WorkThread())
    myUi.setupUi(myMainWindow)
    myUi.startbtn.clicked.connect(lambda: startfun(myUi))
    myUi.opendir.clicked.connect(lambda: os.system('start explorer ' + os.path.join(config.rootDir, "video")))
    try:
        myMainWindow.show()
        myUi.work.start()
        # 线程自定义信号连接的槽函数
        myUi.work.trigger.connect(showresult)
        sys.exit(app.exec_())
    except Exception as e:
        
        print(e)
