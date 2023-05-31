from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QIcon, QAction
from setup_main_window import SetupMainWindow

class MySysTrayWidget(QWidget):
    def __init__(self, ui=None, app=None, window=None):
        QWidget.__init__(self)  # 必须调用，否则信号系统无法启用

        # 私有变量

        self.__app = app
        self.__window = window

        # 配置系统托盘
        self.__trayicon = QSystemTrayIcon(self)
        self.__trayicon.setIcon(QIcon('Resources/logo_top_22x22.ico'))
        self.__trayicon.setToolTip('D22Maid\n热键Ctrl+Alt+M')

        # 创建托盘的右键菜单
        self.__traymenu = QMenu()
        self.__trayaction = []
        self.addTrayMenuAction('Show', self.show_userinterface)
        self.addTrayMenuAction('quit', self.quit)

        # 配置菜单并显示托盘
        self.__trayicon.setContextMenu(self.__traymenu) #把tpMenu设定为托盘的右键菜单
        self.__trayicon.show()  #显示托盘

        # 连接信号
        #self.__ui.pushButton.clicked.connect(self.hide_userinterface)

        # 默认隐藏界面
        self.hide_userinterface()

    def __del__(self):
        pass

    def addTrayMenuAction(self, text='empty', callback=None):
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__traymenu.addAction(a)
        self.__trayaction.append(a)

    def quit(self):
        # 真正的退出
        self.__app.exit()

    def show_userinterface(self):
        self.__window.show()

    def hide_userinterface(self):
        self.__window.hide()