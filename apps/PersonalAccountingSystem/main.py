# -*- coding: utf-8 -*-
# 导入sys
import sys
import mysql.connector
import string
import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui_main import *

from gui.core.json_settings import Settings
from setup_ui import *
from ui_PAS_window import Ui_Dialog
# 继承QWidget类，以获取其属性和方法
class PasswordManagerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.settingFilesFolderPath="apps\PersonalAccountingSystem"

        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        settings = Settings(self.settingFilesFolderPath)
        print("[info]: using",settings.settings_path)
        self.settings = settings.items
        self.projectPath=settings.projectPath


        SetupMainWindow.setup_gui(self)
        # 登录数据库
        self.mydb = mysql.connector.connect(
            host=self.settings["mysql_host"],
            user=self.settings["user"],
            password=self.settings["password"]
        )

        self.cursorObject = self.mydb.cursor()

        createDatabase = "CREATE DATABASE IF NOT EXISTS personal_accounting_system"
        useDatabase = "USE personal_accounting_system"
        createTable = "CREATE TABLE IF NOT EXISTS wallet(id INT PRIMARY KEY,name varchar(50),username varchar(50),password varchar(50), date date,other text,description text);"
        try:
            self.cursorObject.execute(useDatabase)
        except:
            print("[info]: Creating new Database called passwordmanager")

        self.cursorObject.execute(createDatabase)
        self.cursorObject.execute(useDatabase)
        self.cursorObject.execute(createTable)

        self.fetchAllFromDatabase()

        self.uiInitiation()

    def uiInitiation(self):
        pass

    def fetchAllFromDatabase(self):

        # 获取所有数据库信息并打印到表上
        showall = "select * from passwords"

        self.cursorObject.execute(showall)

        result = self.cursorObject.fetchall()
        # print(result)

        for id, name, username, password, date, other, description in result:
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(name))  # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(username))  # Add user
            self.table_widget.setItem(row_number, 2, QTableWidgetItem(password))  # Add pass
            self.table_widget.setItem(row_number, 3, QTableWidgetItem(other))  # Add pass
            self.table_widget.setItem(row_number, 4, QTableWidgetItem(description))
            self.table_widget.setRowHeight(row_number, 22)
        # 刷新上三条统计信息
        self.updateStatistic(result)
        print("[Info]: data all updated from database")


    def deleteCurrentRow(self):
        if self.table_widget.currentRow() != None:
            currentRowIndex = self.table_widget.currentRow()
        else:
            return
        print(currentRowIndex)
        for j in range(5):
            self.table_widget.setItem(currentRowIndex, j, QTableWidgetItem(""))
        # 统计信息

    def updateStatistic(self, result):
        pass
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

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = PasswordManagerWindow()
    print("[info]: Process", window.settings["app_name"], "is starting")
    window.show()

    sys.exit(app.exec())
