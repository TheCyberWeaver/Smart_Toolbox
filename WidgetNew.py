from gui.core.json_settings import Settings
# IMPORT QT CORE
from qt_core import *
# IMPORT SETTINGS
from gui.core.functions import Functions

from setup_main_window import SetupMainWindow
from ui_New import Ui_Form
import os
import sys
from gui.widgets.py_icon_link import *
import json

class WidgetNew(QWidget):
    def __init__(self,parent):
        super().__init__()

        self.mainwindow=parent
        # SETUP MAIN WINDOw
        # Load widgets from "\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("Properties"))

        self.hide_grips = True  # Show/Hide resize grips

        self.ui.pushButton.clicked.connect(lambda: self.openFile())     #路径选择按钮
        self.ui.pushButton_2.clicked.connect(lambda: self.saveFile())   #保存按钮

        self.filePath=""

    def openFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(     #获取选择的路径
            self,
            "Select The Settings File",  # 标题
            r"E:\\",  # 起始目录
            "Type (*.json)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.lineEdit.setText(self.filePath)         #路径栏填写选择的路径

        #将选择路径的setting文件展示到文本框
        with open(self.filePath, "r", encoding='utf-8') as reader:
            settings = reader.read()
        self.ui.textEdit.setText(str(settings))

    def saveFile(self):
        #如果并未填写路径，直接结束子窗口
        if not os.path.isfile(self.filePath):
            print(f"[WARNING]: \"settings.json\" not found! check in the folder {self.filePath}")
            self.close()
            return

        #将文本框内容保存到目标app的setting里
        with open(self.filePath, "w", encoding='utf-8') as writer:
            writer.write(self.ui.textEdit.toPlainText())
        #读取app列表
        with open(Settings().appListSavePaths, "r", encoding='utf-8') as reader:
            applist = json.loads(reader.read())
        #app列表添加目标app并重新写入
        with open(Settings().appListSavePaths, "w+", encoding='utf-8') as file:
            applist.append(self.filePath)
            json.dump(applist, file, indent=4)

        #子程序关闭时刷新主窗口ui，添加的app能立刻显示
        self.mainwindow.ui.setup_ui(self.mainwindow)
        SetupMainWindow.setup_gui(self.mainwindow)

        self.close()