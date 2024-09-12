# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

from gui.widgets.py_icon_link import *
import json
import os
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")


        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////

        self.globalSettings = Settings().globalSettingsItems

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET INITIAL PARAMETERS
        parent.resize(self.globalSettings["startup_size"][0], self.globalSettings["startup_size"][1])
        parent.setMinimumSize(self.globalSettings["minimum_size"][0], self.globalSettings["minimum_size"][1])

        # SET CENTRAL WIDGET
        # Add central widget to app
        # ///////////////////////////////////////////////////////////////
        self.central_widget = QWidget()

        self.central_widget.setStyleSheet(f'''
                            font: {self.globalSettings["font"]["text_size"]}pt "{self.globalSettings["font"]["family"]}";
                            color: {self.themes["app_color"]["text_description"]};
                        ''')

        self.central_widget_layout = QVBoxLayout(self.central_widget)

        if self.globalSettings["custom_title_bar"]:
            self.central_widget_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.central_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.window = PyWindow(
            parent,
            bg_color=self.themes["app_color"]["bg_one"],
            border_color=self.themes["app_color"]["bg_two"],
            text_color=self.themes["app_color"]["text_foreground"]
        )

        # If disable custom title bar
        if not self.globalSettings["custom_title_bar"]:
            self.window.set_stylesheet(border_radius=0, border_size=0)

        # ADD PY WINDOW TO CENTRAL WIDGET
        self.central_widget_layout.addWidget(self.window)



        # ADD TITLE BAR FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM TITLE BAR TO LAYOUT
        self.title_bar = PyTitleBar(
            parent,
            logo_width=45,
            app_parent=self.central_widget,
            logo_image="logo_top_22x22.svg",
            bg_color=self.themes["app_color"]["bg_two"],
            div_color=self.themes["app_color"]["bg_three"],
            btn_bg_color=self.themes["app_color"]["bg_two"],
            btn_bg_color_hover=self.themes["app_color"]["bg_three"],
            btn_bg_color_pressed=self.themes["app_color"]["bg_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_pressed"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            context_color=self.themes["app_color"]["context_color"],
            dark_one=self.themes["app_color"]["dark_one"],
            text_foreground=self.themes["app_color"]["text_foreground"],
            radius=8,
            font_family=self.globalSettings["font"]["family"],
            title_size=self.globalSettings["font"]["title_size"],
            is_custom_title_bar=self.globalSettings["custom_title_bar"]
        )
        self.title_bar_layout.addWidget(self.title_bar)

        self.app_frame = QFrame()

        # ADD RIGHT APP LAYOUT
        self.app_layout = QVBoxLayout(self.app_frame)
        self.app_layout.setContentsMargins(3, 3, 3, 3)
        self.app_layout.setSpacing(6)

        # ADD CONTENT AREA
        # ///////////////////////////////////////////////////////////////
        self.content_area_frame = QFrame()

        # CREATE LAYOUT
        self.content_area_layout = QGridLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)


        # CREDITS / BOTTOM APP FRAME
        # ///////////////////////////////////////////////////////////////
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # CREATE LAYOUT
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)

        # ADD CUSTOM WIDGET CREDITS
        self.credits = PyCredits(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright=self.globalSettings["copyright"],
            version=self.globalSettings["version"],
            font_family=self.globalSettings["font"]["family"],
            text_size=self.globalSettings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"]
        )

        #  ADD TO LAYOUT
        self.credits_layout.addWidget(self.credits)

        # Scan all the app files according to settings.json
        print("[Info][ui_main.py]: Finding all Apps...")
        self.apps_settings_path=Settings().appList  #获取app的setting文件的路径列表
        self.apps_settings=[]                       #存放app的setting文件的内容

        for path in self.apps_settings_path:
            try:
                with open(path, "r", encoding='utf-8') as reader:
                    self.apps_settings.append(json.loads(reader.read()))

            except FileNotFoundError:
                print("[Error][ui_main.py]: "+path+" Not Found")
            except json.decoder.JSONDecodeError:
                print("[Error][ui_main.py]: "+path+" read error")
                continue
        self.apps=[]        #存放app的UI控件

        for setting_file_index in range(len(self.apps_settings)):
            #判断是否存在appsettings所包含的启动文件
            if not os.path.isfile(self.apps_settings[setting_file_index]["app_main"]):
                print("[Warning][ui_main.py]: could not fin app: ",self.apps_settings[setting_file_index]["app_main"])
            else:
                print("[Info][ui_main.py]: found app: ",self.apps_settings[setting_file_index]["app_main"])
            #添加一个app控件
            app=PyIconLink(self,
                           lnk_path=self.apps_settings[setting_file_index]["app_main"],
                           icon_path=self.apps_settings[setting_file_index]["icon"],
                           settings_path=self.apps_settings_path[setting_file_index],
                           globalAppListSavePath=Settings().appListSavePaths
                           )
            self.apps.append(app)


        #控制app控件每行显示的数量
        count=0
        row=0
        self.maximumAppsInOneRow=self.globalSettings["maximum_apps_in_one_row"]
        for row in range(len(self.apps)):
            for column in range(self.maximumAppsInOneRow):
                if count>=len(self.apps):
                    break
                self.content_area_layout.addWidget(self.apps[count],row,column)
                count+=1
            row += 1


        # ADD WIDGETS TO RIGHT LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.app_layout.addWidget(self.title_bar_frame)
        self.app_layout.addWidget(self.content_area_frame)
        self.app_layout.addWidget(self.credits_frame)

        # ADD WIDGETS TO "PyWindow"
        # Add here your custom widgets or default widgets
        # ///////////////////////////////////////////////////////////////
        self.window.layout.addWidget(self.app_frame)
        # ADD CENTRAL WIDGET AND SET CONTENT MARGINS
        # ///////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.central_widget)
