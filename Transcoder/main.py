from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PluginManager import *
from gui.core.json_settings import Settings


class Transcoderpage(QMainWindow):

    def __init__(self, loadpage):
        super().__init__()
        self.Methods_manager = CoderPluginManager()
        self.Methods_manager.loadPlugins()      #加载所有编码插件

        settings = Settings()
        self.settings = settings.items

        # print(self.Methods_manager.getPluginsName())
        self.ui = loadpage
        self.uiInitiation()

        self.final = ''     #最终输出的字符串
        self.original = ''  #读入的字符串
        self.key = ""       #读入的key
        self.method = CoderInterface()
        self.Mode = 2   #当前是编码:2 还是解码:1
        self.filelist = []
        self.outputInfo = ""    #输出的info

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
        # 修复Label字体不统一的问题
        """font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        self.ui.label_2.setFont(font)
        self.ui.page_1.setStyleSheet("QLabel{font-size: 18pt;"
                                     "font-family: \"Impact\"}")"""
        # 处理搜索清除按钮
        self.ui.ClearButton.clicked.connect(self.ui.lineEdit.clear)

        # self.ui.page_1.setStyleSheet(f'''
        #                            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
        #                        ''')
        # 默认编码encode
        self.ui.encode.setChecked(True)

    def SmartConversion(self):
        self.ManualConversion()

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

        # 输出编码后的字符串
        self.output()

    def showInfo(self):
        text = "version:" + self.method.version + "\n\n" + self.method.Description
        self.ui.output_text_edit_2.setText(text)
    #更新编码族列表
    def update_list(self):
        templist = []
        str = self.ui.lineEdit.text()
        for method_name in self.Methods_manager.getPluginsName():
            if method_name.lower().find(str.lower()) != -1 or method_name.upper().find(str.upper()) != -1:
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
    #读入搜索框
    def input(self):
        self.original = self.ui.input_text_edit.toPlainText()
    #读入key
    def inputKey(self):
        self.key = self.ui.input_text_edit_2.toPlainText()
    #输出final string
    def output(self):
        self.ui.output_text_edit.setText(self.final)

    #获取编码还是解码
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

    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette()))
    window.show()  # 显示窗口

    sys.exit(app.exec())
