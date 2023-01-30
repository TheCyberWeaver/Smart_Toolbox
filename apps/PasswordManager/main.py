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
from ui_PasswordManager import Ui_Dialog
# 继承QWidget类，以获取其属性和方法
class PasswordManagerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.settingFilesFolderPath="apps\PasswordManager"

        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        settings = Settings(self.settingFilesFolderPath)
        print("[info]: using",settings.settings_path)
        self.settings = settings.items
        self.projectPath=settings.projectPath

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        #self.hide_grips = True  # Show/Hide resize grips

        SetupMainWindow.setup_gui(self)
        # 登录数据库
        self.mydb = mysql.connector.connect(
            host=self.settings["mysql_host"],
            user=self.settings["user"],
            password=self.settings["password"]
        )

        self.cursorObject = self.mydb.cursor()

        createDatabase = "CREATE DATABASE IF NOT EXISTS passwordmanager"
        useDatabase = "USE passwordmanager"
        createTable = "CREATE TABLE IF NOT EXISTS passwords(id INT PRIMARY KEY,name varchar(50),username varchar(50),password varchar(50), date date,other text,description text);"
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
        self.icon_button_1.clicked.connect(lambda: self.fetchAllFromDatabase())
        self.push_button_1.clicked.connect(lambda: self.saveAll())
        self.push_button_2.clicked.connect(lambda: self.table_widget.insertRow(self.table_widget.rowCount()))
        self.push_button_3.clicked.connect(lambda: self.deleteCurrentRow())

    def fetchAllFromDatabase(self):

        # 保留表头
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)
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

    def saveAll(self):

        self.cursorObject.execute("DELETE FROM passwords")  # 先删除整个表，然后重新填写，逻辑最简单，保证数据库id完整性，没有跳行
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        row_number = self.table_widget.rowCount()
        databaseID = 1  # 循环变量，用于表示数据库内当前应当存放的id
        for i in range(row_number):
            if self.table_widget.item(i, 0) == None:
                name = ""  # 如果item为空特殊处理 #懒得整理逻辑，直接复制
            else:
                name = self.table_widget.item(i, 0).text()

            if self.table_widget.item(i, 1) == None:
                username = ""
            else:
                username = self.table_widget.item(i, 1).text()

            if self.table_widget.item(i, 2) == None:
                password = ""
            else:
                password = self.table_widget.item(i, 2).text()

            if self.table_widget.item(i, 3) == None:
                other = ""
            else:
                other = self.table_widget.item(i, 3).text()

            if self.table_widget.item(i, 4) == None:
                description = ""
            else:
                description = self.table_widget.item(i, 4).text()

            description = description.strip()  # description最后会有\r，我也不知道为什么,需要在拼接字符串前将其删除

            if name == "" and username == "" and password == "" and other == "" and description == "":  # 如果一整行为空则放弃insert这一行，数据库id不会改变
                continue

            """insert="INSERT INTO passwords (id,name,username,password,date,other,description) values ("\
                   +str(databaseID)+",\'"+name +"\' , \'"+username+"\' , \'"+password+"\' , \'"+date+"\' , \'"+other+"\' , \'"+description+\
                   "\')ON DUPLICATE KEY UPDATE " \
                   "id="+str(databaseID)+",name= \'"+name+"\'"+",username= \'"+username+"\'"+",password= \'"+password+"\'"+",date= \'"+date+"\'"+",other= \'"+other+"\'"+",description= \'"+description+"\'"+";" """

            insert = "INSERT INTO passwords (id,name,username,password,date,other,description) values (" \
                     + str(
                databaseID) + ",\'" + name + "\' , \'" + username + "\' , \'" + password + "\' , \'" + date + "\' , \'" + other + "\' , \'" + description + "\')"  # 加入这一行
            self.cursorObject.execute(insert)
            # print(insert)
            databaseID += 1

        print("[Info]: save all data to database")
        self.fetchAllFromDatabase()  # 保存后刷新数据

        self.mydb.commit()  # 提交数据，否则DDL语句不会自动commit

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

        strength = 0
        leakedcount = 0

        f = open(os.path.join(self.projectPath,"Resources/All_List.txt"), 'r')
        leakedList = f.readlines()
        f.close()

        savedList = []
        for id, name, username, password, date, other, description in result:
            strength += self.passwordStrength(password)
            if password in savedList:
                leakedcount += 1
            else:
                for word in leakedList:
                    if password == word.rstrip("\n"):
                        leakedcount += 1
                        savedList.append(password)
                        break
        # print(savedList)

        percentage = int(strength / (4 * len(result)) * 100)
        self.circular_progress_1.set_value(len(result))
        self.circular_progress_2.set_value(percentage)
        # print(leakedcount)
        self.circular_progress_3.set_value(int(leakedcount / len(result) * 100))

        # 计算单条密码的复杂度

    def passwordStrength(self, str):

        password = str

        dig = 0
        lCase = 0
        hCase = 0
        punnctuation = 0

        if len(password) <= 8:
            return 0
        else:
            for ch in password:
                if ch in string.digits:
                    dig = 1
                elif ch in string.ascii_lowercase:
                    lCase = 1
                elif ch in string.ascii_uppercase:
                    hCase = 1
                elif ch in string.punctuation:
                    punnctuation = 1
            return dig + lCase + hCase + punnctuation

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
