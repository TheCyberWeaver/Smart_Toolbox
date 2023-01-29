# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(803, 543)
        self.verticalLayout_4 = QVBoxLayout(MainPages)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 430, 301, 41))
        self.listWidget = QListWidget(self.page_1)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 60, 181, 111))
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.output_text_edit_2 = QTextEdit(self.page_1)
        self.output_text_edit_2.setObjectName(u"output_text_edit_2")
        self.output_text_edit_2.setGeometry(QRect(30, 300, 211, 181))
        self.input_text_edit = QPlainTextEdit(self.page_1)
        self.input_text_edit.setObjectName(u"input_text_edit")
        self.input_text_edit.setGeometry(QRect(260, 50, 531, 131))
        self.input_text_edit.setBackgroundVisible(False)
        self.lineEdit = QLineEdit(self.page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 10, 131, 31))
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 200, 41, 31))
        self.label_4.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.output_text_edit = QTextEdit(self.page_1)
        self.output_text_edit.setObjectName(u"output_text_edit")
        self.output_text_edit.setGeometry(QRect(260, 300, 531, 111))
        self.input_text_edit_2 = QPlainTextEdit(self.page_1)
        self.input_text_edit_2.setObjectName(u"input_text_edit_2")
        self.input_text_edit_2.setGeometry(QRect(310, 200, 481, 31))
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 81, 28))
        self.label_3.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.encode = QRadioButton(self.page_1)
        self.encode.setObjectName(u"encode")
        self.encode.setGeometry(QRect(400, 250, 91, 41))
        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 420, 221, 51))
        self.decode = QRadioButton(self.page_1)
        self.decode.setObjectName(u"decode")
        self.decode.setGeometry(QRect(510, 248, 101, 41))
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 250, 121, 41))
        self.label_2.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 250, 171, 41))
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 10, 171, 31))
        self.label_6.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 270, 41, 21))
        self.label_5.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 121, 31))
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.listWidget_2 = QListWidget(self.page_1)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(30, 180, 181, 81))
        font = QFont()
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.ClearButton = QPushButton(self.page_1)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(190, 10, 21, 31))
        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 32))
        self.label_8.setStyleSheet(u"font: 700 18pt \"Segoe Print\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"	border-top:2px solid #C2C7CB;\n"
"	position:absolute;\n"
"	top:-10px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u5c45\u4e2d */\n"
"QTabWidget::tab-bar {\n"
"	alignment:center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"	border:2px solid #C4C4C3;\n"
"	border-bottom-color:#C2C7CB;\n"
"	border-top-left-radius:4px;\n"
"	border-top-right-radius:4px;\n"
"	min-width:20px;\n"
"	padding:2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover {\n"
"	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-color:#9B9B9B;\n"
"	border-bottom-color:#C2C7CB;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 32))
        self.label_11.setStyleSheet(u"font: 700 18pt \"Segoe Print\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 12))
        self.label_12.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 12))
        self.label_13.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.pages.addWidget(self.page_3)

        self.verticalLayout_4.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainPages", u"Declaration", None))
        self.input_text_edit.setPlainText("")
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Key", None))
        self.input_text_edit_2.setPlainText("")
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Search", None))
        self.encode.setText(QCoreApplication.translate("MainPages", u"Encode", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPages", u"Smart Conversion (beta)", None))
        self.decode.setText(QCoreApplication.translate("MainPages", u"Decode", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Output Text", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"Convert", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Using:", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Input Text", None))
        self.ClearButton.setText(QCoreApplication.translate("MainPages", u"X", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Password Manager", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"number count", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"passwords strength", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"leaked passwords", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"Linear Algebra", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Vector Field Visualization", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"Eigenvector and Eigenvalue", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Inner Product", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainPages", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainPages", u"Tab 2", None))
    # retranslateUi

