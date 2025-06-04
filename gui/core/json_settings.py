# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os
from pathlib import Path


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self, settings_path="default"):
        super(Settings, self).__init__()

        self.projectPath = self.get_project_path()
        self.json_file = "settings.json"                #统一的config文件名称
        self.appListSavePaths = os.path.join(self.projectPath,"applist.json")   #所有app路径的记录文件的路径

        self.globleSettingsPath = os.path.join(self.projectPath, self.json_file)     #

        if not os.path.isfile(self.globleSettingsPath):
            print(f"[WARNING]: \"settings.json\" not found! check in the folder {self.globleSettingsPath}")

        #获取smarttoolbox本身的setting条目
        self.globalSettingsItems = {}

        with open(self.globleSettingsPath, "r", encoding='utf-8') as reader:
            self.globalSettingsItems = json.loads(reader.read())

        #存放所有app的setting.json的路径
        self.appList=[]

        with open(self.appListSavePaths, "r", encoding='utf-8') as reader:
            self.appList = json.loads(reader.read())

    #获取当前项目路径，获取文件绝对路径再减去项目名称，因此项目名称不可改变
    def get_project_path(self):
        """Return project root path.

        The previous implementation searched for a hard coded folder name
        (``Smarttoolbox``) inside the current path. When the project folder
        name differs, ``str.index`` raises ``ValueError`` and the application
        crashes.  Instead of relying on the folder name, determine the project
        root relative to this file location.
        """

        # ``json_settings.py`` lives in ``<root>/gui/core``.  ``parents[2]``
        # will therefore point to the repository root regardless of its
        # actual name.
        return str(Path(__file__).resolve().parents[2])
