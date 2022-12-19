import mysql.connector
import string

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from gui.core.json_settings import Settings
from gui.uis.pages.ui_main_pages import Ui_MainPages

from gui.uis.windows.main_window import *

class Passwordmanager(QMainWindow):

    def __init__(self, loadpage):
        super().__init__()
        self.ui=loadpage
        settings = Settings()
        self.settings = settings.items



        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="7bf9108cd896f33C!"
        )
        self.cursorObject = self.mydb.cursor()
        createDatabases = "CREATE DATABASE IF NOT EXISTS passwordmanager"
        useDatabase = "USE passwordmanager"
        createTable = "CREATE TABLE IF NOT EXISTS passwords(id INT,name varchar(50),username varchar(50),password varchar(50), date date,other text,description text);"
        self.cursorObject.execute(createDatabases)
        self.cursorObject.execute(useDatabase)
        self.cursorObject.execute(createTable)

        self.getAll()

        self.uiInitiation()

    def uiInitiation(self):
        self.ui.left_btn_1.clicked.connect(self.getAll())

    def getAll(self):

        showall = "select * from passwords"

        self.cursorObject.execute(showall)

        result = self.cursorObject.fetchall()
        print(result)
        for id, name, username, password, date, other, description in result:
            row_number = self.ui.table_widget.rowCount()
            self.ui.table_widget.insertRow(row_number)  # Insert row
            self.ui.table_widget.setItem(row_number, 0, QTableWidgetItem(name))  # Add name
            self.ui.table_widget.setItem(row_number, 1, QTableWidgetItem(username))  # Add user
            self.ui.table_widget.setItem(row_number, 2, QTableWidgetItem(password))  # Add pass
            self.ui.table_widget.setItem(row_number, 3, QTableWidgetItem(other))  # Add pass
            self.ui.table_widget.setRowHeight(row_number, 22)
        self.updateStatistic(result)

    def updateStatistic(self,result):


        strength = 0
        pawndcount=0

        f=open("Resources/All_List.txt",'r')
        leakedList=f.readlines()
        f.close()

        savedList=[]
        for id, name, username, password, date, other, description in result:
            strength += self.passwordStrength(password)
            if password in savedList:
                pawndcount += 1
            else:
                for word in leakedList:
                    if password == word.rstrip("\n"):
                        pawndcount += 1
                        savedList.append(password)
                        break
        print(savedList)

        percentage = int(strength / (4 * len(result)) * 100)
        self.ui.circular_progress_1.set_value(len(result))
        self.ui.circular_progress_2.set_value(percentage)
        print(pawndcount)
        self.ui.circular_progress_3.set_value(int(pawndcount/len(result)*100))


    def passwordStrength(self,str):

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

