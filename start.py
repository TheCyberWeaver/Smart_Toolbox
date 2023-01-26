# IMPORT PACKAGES AND MODULES
from gui.uis.windows.main_window.functions_main_window import *
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


class Container(QWidget):
    double_clicked = Signal(QWidget)
    rows = 3
    cols = 6
    item_width = 42
    spacing = 20
    height = rows*item_width + (rows+1)*spacing
    width = cols*item_width + (cols+1)*spacing

    def __init__(self, parent=None):
        super(Container, self).__init__(parent=parent)

        self.items = []

        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setOffset(0, 0)
        shadow_effect.setColor(Qt.gray)
        shadow_effect.setBlurRadius(20)
        self.setGraphicsEffect(shadow_effect)

    def set_items(self, lnk_paths):
        self.items = []
        for lnk_path in lnk_paths:
            item = PyIconLink(self, lnk_path)
            item.setFixedSize(self.item_width, self.item_width)
            item.double_clicked.connect(self.double_clicked.emit)
            item.show()
            self.items.append(item)
        self.update_items()

    def add_item(self, lnk_path):
        item = PyIconLink(self, lnk_path)
        item.setFixedSize(self.item_width, self.item_width)
        item.double_clicked.connect(self.double_clicked.emit)
        item.show()
        self.items.append(item)
        self.update_items()

    def remove_item(self, item):
        item.deleteLater()
        self.items.remove(item)
        self.update_items()

    def update_items(self):
        row = 0
        col = 0
        for t in self.items:
            x = col * (self.spacing + self.item_width) + self.spacing
            y = row * (self.spacing + self.item_width) + self.spacing
            t.setGeometry(x, y, self.item_width, self.item_width)
            col += 1
            row += col // self.cols
            col %= self.cols
        self.repaint()

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        settings = Settings()
        self.settings = settings.items

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
    app.setWindowIcon(QIcon("icon.ico"))
    window = Launcher()  # 实例化一个主窗口

    window.show()  # 显示窗口

    sys.exit(app.exec())  # 使窗口保持显示状态。