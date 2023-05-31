# IMPORT PACKAGES AND MODULES
#from gui.uis.windows.main_window.functions_main_window import *
from gui.core.json_settings import Settings
# IMPORT QT CORE
from qt_core import *
# IMPORT SETTINGS
from gui.core.functions import Functions
from ui_main import UI_MainWindow
from setup_main_window import SetupMainWindow
from ui_New import Ui_Form
from WidgetNew import WidgetNew
import os
import sys

from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QIcon, QAction
from gui.widgets.py_icon_link import *
from exe_IconExtraction import get_icon_from_exe

from Tray import MySysTrayWidget

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        # LOAD SETTINGS using gloabal setting.json
        settings = Settings()
        self.settings = settings.globalSettingsItems
        self.setWindowIcon(QIcon(self.settings["icon"]))

        self.hide_grips = True  # Show/Hide resize grips

        SetupMainWindow.setup_gui(self)

        self.createContextMenu() #right click menu

    def createContextMenu(self):
        # 处理右键信号，必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        self.contextMenu = QMenu(self)
        self.contextMenu.setStyleSheet("font: 12pt \"Segoe UI\";")

        self.action_Add = self.contextMenu.addAction('ADD')
        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.action_Add.triggered.connect(self.addAppFromUser)

    def showContextMenu(self, pos):
        '''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(QtGui.QCursor().pos())
        self.contextMenu.show()

    def addAppFromUser(self):
        '''
            添加app，显示子窗口
        '''
        print("[Info][start.py]: add cllicked")

        self.propertyWindow=WidgetNew(self)
        self.propertyWindow.show()
    def btn_clicked(self):
        # GET CLICKED
        btn = SetupMainWindow.setup_btns(self)

        if btn.objectName() == "btn_search":
            print("hello")

    def btn_released(self):
        # GET CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def closeEvent(self, event):
        # 忽略退出事件，而是隐藏到托盘
        event.ignore()
        self.hide()
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 实例化一个应用

    app.processEvents()

    window = Launcher()  # 实例化一个主窗口

    window.show()  # 显示窗口

    tray = MySysTrayWidget(app=app, window=window)
    sys.exit(app.exec())  # 使窗口保持显示状态。