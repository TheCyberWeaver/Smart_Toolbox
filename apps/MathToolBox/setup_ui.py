# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from qt_core import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from ui_main import UI_MainWindow
import os
# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)



    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////

        self.setWindowTitle(self.settings["app_name"])
        self.setWindowIcon(QtGui.QIcon(self.settings["icon"]))
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings(self.settingFilesFolderPath)
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes(self.settingFilesFolderPath)
        self.themes = themes.items

        self.push_button_4 = PyPushButton(
            text="Run",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_4.setMaximumHeight(30)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text="",
            place_holder_text="u(x,y)",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)
        self.line_edit.setMaximumWidth(200)

        self.line_edit_2 = PyLineEdit(
            text="",
            place_holder_text="v(x,y)",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_2.setMinimumHeight(30)
        self.line_edit_2.setMaximumWidth(200)

        self.line_edit_3 = PyLineEdit(
            text="",
            place_holder_text="X Minimum",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_3.setMinimumHeight(30)
        self.line_edit_3.setMaximumWidth(150)

        self.line_edit_4 = PyLineEdit(
            text="",
            place_holder_text="X Maximum",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_4.setMinimumHeight(30)
        self.line_edit_4.setMaximumWidth(150)

        self.line_edit_5 = PyLineEdit(
            text="",
            place_holder_text="Y Minimum",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_5.setMinimumHeight(30)
        self.line_edit_5.setMaximumWidth(150)

        self.line_edit_6 = PyLineEdit(
            text="",
            place_holder_text="Y Maximum",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_6.setMinimumHeight(30)
        self.line_edit_6.setMaximumWidth(150)

        self.ui.verticalLayout_7.addWidget(self.push_button_4)

        self.ui.verticalLayout_4.addWidget(self.line_edit)
        self.ui.verticalLayout_4.addWidget(self.line_edit_2)

        self.ui.verticalLayout_6.addWidget(self.line_edit_3)
        self.ui.verticalLayout_6.addWidget(self.line_edit_4)
        self.ui.verticalLayout_6.addWidget(self.line_edit_5)
        self.ui.verticalLayout_6.addWidget(self.line_edit_6)