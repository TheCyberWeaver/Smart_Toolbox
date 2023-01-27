# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
# PROJECT MADE WITH: Qt Designer and PySide6
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

import mysql.connector
import string
import time
import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from gui.core.json_settings import Settings


class PersonalAccountingSystem(QMainWindow):

    def __init__(self, loadpage):
        super().__init__()
        self.ui=loadpage    #所有setup_main_window.py的组件都被放在self.ui里
        settings = Settings()
        self.settings = settings.items


        #登录数据库
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="7bf9108cd896f33C!"
        )

        self.cursorObject = self.mydb.cursor()
        createDatabases = "CREATE DATABASE IF NOT EXISTS personalaccountingsystem"
        useDatabase = "USE personalaccountingsystem"
        createTable_Wallet = "CREATE TABLE IF NOT EXISTS wallet(id INT PRIMARY KEY,name varchar(50),current_money varchar(50),description text);"
        createTable_Transaction = "CREATE TABLE IF NOT EXISTS Transaction(id INT PRIMARY KEY,wallet_name varchar(50),money varchar(50),date date);"
        createTable_Card = "CREATE TABLE IF NOT EXISTS Card(id INT PRIMARY KEY,card_name varchar(50),information_string(100),description text);"
        self.cursorObject.execute(createDatabases)
        self.cursorObject.execute(useDatabase)
        self.cursorObject.execute(createTable_Wallet)
        self.cursorObject.execute(createTable_Transaction)
        self.cursorObject.execute(createTable_Card)

        self.fetchAllFromDatabase()

        self.uiInitiation()

    def uiInitiation(self):
        pass
    def fetchAllFromDatabase(self):

        #保留表头
        self.ui.table_widget.clearContents()
        self.ui.table_widget.setRowCount(0)
        #获取所有数据库信息并打印到表上
        showall = "select * from passwords"

        self.cursorObject.execute(showall)

        result = self.cursorObject.fetchall()
        #print(result)

        for id, name, username, password, date, other, description in result:
            row_number = self.ui.table_widget.rowCount()
            self.ui.table_widget.insertRow(row_number)  # Insert row
            self.ui.table_widget.setItem(row_number, 0, QTableWidgetItem(name))  # Add name
            self.ui.table_widget.setItem(row_number, 1, QTableWidgetItem(username))  # Add user
            self.ui.table_widget.setItem(row_number, 2, QTableWidgetItem(password))  # Add pass
            self.ui.table_widget.setItem(row_number, 3, QTableWidgetItem(other))  # Add pass
            self.ui.table_widget.setItem(row_number, 4, QTableWidgetItem(description))
            self.ui.table_widget.setRowHeight(row_number, 22)
        #刷新上三条统计信息
        self.updateStatistic(result)
        print("[Info]: data all updated from database")
    def saveAll(self):

        self.cursorObject.execute("DELETE FROM passwords")      #先删除整个表，然后重新填写，逻辑最简单，保证数据库id完整性，没有跳行
        date=time.strftime('%Y-%m-%d', time.localtime(time.time()))

        row_number = self.ui.table_widget.rowCount()
        databaseID=1 #循环变量，用于表示数据库内当前应当存放的id
        for i in range(row_number):
            if self.ui.table_widget.item(i,0)==None: name=""    #如果item为空特殊处理 #懒得整理逻辑，直接复制
            else: name=self.ui.table_widget.item(i,0).text()

            if self.ui.table_widget.item(i,1)==None: username=""
            else: username=self.ui.table_widget.item(i,1).text()

            if self.ui.table_widget.item(i,2)==None: password=""
            else: password=self.ui.table_widget.item(i,2).text()

            if self.ui.table_widget.item(i,3)==None: other=""
            else: other=self.ui.table_widget.item(i,3).text()

            if self.ui.table_widget.item(i,4)==None: description=""
            else: description=self.ui.table_widget.item(i,4).text()

            description=description.strip()     #description最后会有\r，我也不知道为什么,需要在拼接字符串前将其删除

            if name=="" and username=="" and password=="" and other=="" and description=="": #如果一整行为空则放弃insert这一行，数据库id不会改变
                continue

            """insert="INSERT INTO passwords (id,name,username,password,date,other,description) values ("\
                   +str(databaseID)+",\'"+name +"\' , \'"+username+"\' , \'"+password+"\' , \'"+date+"\' , \'"+other+"\' , \'"+description+\
                   "\')ON DUPLICATE KEY UPDATE " \
                   "id="+str(databaseID)+",name= \'"+name+"\'"+",username= \'"+username+"\'"+",password= \'"+password+"\'"+",date= \'"+date+"\'"+",other= \'"+other+"\'"+",description= \'"+description+"\'"+";" """

            insert="INSERT INTO passwords (id,name,username,password,date,other,description) values ("\
                   +str(databaseID)+",\'"+name +"\' , \'"+username+"\' , \'"+password+"\' , \'"+date+"\' , \'"+other+"\' , \'"+description+"\')"    #加入这一行
            self.cursorObject.execute(insert)
            #print(insert)
            databaseID+=1

        print("[Info]: save all data to database")
        self.fetchAllFromDatabase()   #保存后刷新数据

        self.mydb.commit()  #提交数据，否则DDL语句不会自动commit

    def deleteCurrentRow(self):
        print("hello")
        if self.ui.table_widget.currentRow()!=None:
            currentRowIndex=self.ui.table_widget.currentRow()
        else:
            return
        print(currentRowIndex)
        for j  in range(5):
            self.ui.table_widget.setItem(currentRowIndex,j,QTableWidgetItem(""))


# 主函数main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PersonalAccountingSystem()

    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6', palette=LightPalette()))
    window.show()  # 显示窗口

    sys.exit(app.exec())