# IMPORT PACKAGES AND MODULES
#from gui.uis.windows.main_window.functions_main_window import *
from gui.core.json_settings import Settings
# IMPORT QT CORE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from PySide6 import QtGui
# IMPORT SETTINGS
from gui.core.functions import Functions
from ui_main import UI_MainWindow
from setup_main_window import SetupMainWindow

import os
import sys
from gui.widgets.py_icon_link import *
from exe_IconExtraction import get_icon_from_exe




class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        settings = Settings("global")
        self.settings = settings.items
        self.setWindowIcon(QIcon(self.settings["icon"]))
        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)




    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        if btn.objectName() == "btn_search":
            print("hello")

    def btn_released(self):
        # GET BT CLICKED
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
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 实例化一个应用

    app.processEvents()

    window = Launcher()  # 实例化一个主窗口

    window.show()  # 显示窗口

    sys.exit(app.exec())  # 使窗口保持显示状态。