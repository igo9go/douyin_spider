# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'douyinui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, worker):
        self.work = worker
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.zuozheel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zuozheel.sizePolicy().hasHeightForWidth())
        self.zuozheel.setSizePolicy(sizePolicy)
        self.zuozheel.setMinimumSize(QtCore.QSize(0, 35))
        self.zuozheel.setObjectName("zuozheel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.zuozheel)
        self.zuozheinput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zuozheinput.sizePolicy().hasHeightForWidth())
        self.zuozheinput.setSizePolicy(sizePolicy)
        self.zuozheinput.setMinimumSize(QtCore.QSize(0, 35))
        self.zuozheinput.setSizeIncrement(QtCore.QSize(0, 35))
        self.zuozheinput.setObjectName("zuozheinput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zuozheinput)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.videoel = QtWidgets.QLabel(self.centralwidget)
        self.videoel.setMinimumSize(QtCore.QSize(0, 35))
        self.videoel.setObjectName("videoel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.videoel)
        self.videoinput = QtWidgets.QLineEdit(self.centralwidget)
        self.videoinput.setMinimumSize(QtCore.QSize(0, 35))
        self.videoinput.setText("")
        self.videoinput.setObjectName("videoinput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.videoinput)
        
        '''
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        #self.videoNums = QtWidgets.QLineEdit(self.centralwidget)
        #self.videoNums.setMinimumSize(QtCore.QSize(0, 35))
        #self.videoNums.setObjectName("videoNums")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.videoNums)
        '''
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.formLayout_2)
       
        
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy)
        self.startbtn.setMinimumSize(QtCore.QSize(150, 40))
        self.startbtn.setObjectName("startbtn")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.startbtn)
        self.opendir = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opendir.sizePolicy().hasHeightForWidth())
        self.opendir.setSizePolicy(sizePolicy)
        self.opendir.setMinimumSize(QtCore.QSize(200, 40))
        self.opendir.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none")
        self.opendir.setObjectName("opendir")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.opendir)
        self.textel = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textel.sizePolicy().hasHeightForWidth())
        self.textel.setSizePolicy(sizePolicy)
        self.textel.setMinimumSize(QtCore.QSize(0, 400))
        self.textel.setStyleSheet("background:rgba(0,0,0,0);")
        self.textel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textel.setObjectName("textel")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.textel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抖音采集"))
        MainWindow.setStatusTip(_translate("MainWindow", "抖音采集"))
        self.zuozheel.setText(_translate("MainWindow", "作者主页url："))
        self.zuozheinput.setPlaceholderText(_translate("MainWindow", "抖音app-右上角点击-分享主页-复制链接"))
        self.videoel.setText(_translate("MainWindow", "单个视频url："))
        self.videoinput.setPlaceholderText(_translate("MainWindow", "抖音app-分享按钮-复制链接"))
        #self.label.setText(_translate("MainWindow", "爬取数量："))
        #self.videoNums.setPlaceholderText(_translate("MainWindow", "从作者主页爬取的视频数量，默认500"))
        self.startbtn.setText(_translate("MainWindow", "开始"))
        self.opendir.setText(_translate("MainWindow", "打开视频目录"))
