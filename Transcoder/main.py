import sys, os
import hashlib

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from .methods import *

import qdarkstyle
from qdarkstyle.light.palette import LightPalette
from gui.uis.pages.main_pages import Ui_MainPages
class Transcoderpage(QMainWindow):

    def __init__(self,loadpage):
        super().__init__()
        self.Methods_manager = CoderPluginManager()
        self.Methods_manager.loadPlugins()

        # print(self.Methods_manager.getPluginsName())
        self.ui = loadpage
        self.uiInitiation()

        self.final = ''
        self.original = ''
        self.key = ""
        self.method = CoderInterface()
        self.Mode = 2
        self.filelist = []
        self.outputInfo = ""

    def uiInitiation(self):

        # self.ui.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止修改item
        # 初始化列表
        self.showList(self.ui.listWidget, self.Methods_manager.getPluginsName())

        # 一旦文字改变便刷新item
        self.ui.lineEdit.textChanged.connect(self.update_list)
        # 处理单击双击选中类别item时
        self.ui.listWidget.itemClicked.connect(self.setMethodFamily)
        self.ui.listWidget.itemDoubleClicked.connect(self.setMethodFamily)
        # 处理单击双击选中具体成员item时
        self.ui.listWidget_2.itemClicked.connect(self.setMethodMember)
        self.ui.listWidget_2.itemDoubleClicked.connect(self.setMethodMember)
        # 连接start和convert按钮
        self.ui.pushButton.clicked.connect(self.ManualConversion)
        #修复文字背景为白色的问题
        self.ui.label_2.setStyleSheet("""background-color: transparent;""")
        # 默认方式
        self.ui.encode.setChecked(True)

    def SmartConversion(self):
        pass

    def ManualConversion(self):

        # 获取输入框内的字符串
        self.input()
        self.output()
        self.inputKey()
        self.method.setKey(self.key)
        # print(self.final)
        # 获取此时的方法
        self.Mode = self.getMode()
        # print(self.de_en,self.method)

        # 判断使用什么方法
        self.use_methods()
        # 输出编码后的字符串
        self.output()

    def showInfo(self):
        text="version:"+self.method.version+"\n\n"+self.method.Description
        self.ui.output_text_edit_2.setText(text)

    def update_list(self):
        templist = []
        str = self.ui.lineEdit.text()
        for method_name in self.Methods_manager.getPluginsName():
            if method_name.find(str) != -1:
                templist.append(method_name)
        self.showList(self.ui.listWidget, templist)

    def setMethodFamily(self, qModelIndex):
        self.method = self.Methods_manager.getPlugin(qModelIndex.text())
        self.ui.lineEdit.setText(self.method.Name)
        self.showMethodMember()
        self.showInfo()

    def setMethodMember(self, qModelIndex):
        self.method.setFamilyMember(qModelIndex.text())

    def showMethodMember(self):
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.method.FamilyMembers)

    def showList(self, listWidget, list):
        listWidget.clear()
        for str in list:
            listWidget.addItem(str)

    # 输入与输出
    def input(self):
        self.original = self.ui.input_text_edit.toPlainText()

    def inputKey(self):
        self.key = self.ui.input_text_edit_2.toPlainText()

    def output(self):
        self.ui.output_text_edit.setText(self.final)

    def use_methods(self):

        self.method._setString(self.original)
        # 编码encode
        if self.Mode == 2:
            if self.method.Name == '':
                self.final = 'Hey, select a function to encode, stupid!!!'
            self.final = self.method.encode()

        # 解码decode
        elif self.Mode == 1:
            if self.method.Name == '':
                self.final = 'Hey, select a function to decode, stupid!!!'
            self.final = self.method.decode()
        else:
            pass

    def getMode(self):
        if self.ui.encode.isChecked():
            return 2
        else:
            return 1

    # 键盘响应
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return:
            self.ManualConversion()


# 主函数main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Transcoderpage()

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette()))
    window.show()  # 显示窗口

    sys.exit(app.exec())
