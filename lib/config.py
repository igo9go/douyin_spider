import os
# 执行过程消息反馈
message=[]
# 从作者主页获取的数量
videoNums=500

# 版本 chromedriver playwright
type=""

# 所有的videourls 播放页面
videourls=[]

# 所有的title和视频下载url {title:,url:}
downloads=[]

# 是否组件 浏览器等符合条件，符号才允许继续执行
Yescan=False
# user-agent头
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# 代理
proxies={}

# 线程数量
threadNums=5

# 项目入口目录
rootDir=os.path.realpath("./")

# 存储路径
saveDir= os.path.join(rootDir, "video")
if not os.path.exists(saveDir):
    os.mkdir(saveDir)
logsDir=os.path.join(rootDir, "logs")
if not os.path.exists(logsDir):
    os.mkdir(logsDir)

binDir=  os.path.join(rootDir,'bin')


# 当前运行状态
runing=False

# textel 空集
textel=None