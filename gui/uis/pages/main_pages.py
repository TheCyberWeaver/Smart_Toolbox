# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(803, 511)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 801, 511))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 430, 301, 41))
        self.listWidget = QListWidget(self.page_1)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 60, 181, 111))
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.output_text_edit_2 = QTextEdit(self.page_1)
        self.output_text_edit_2.setObjectName(u"output_text_edit_2")
        self.output_text_edit_2.setGeometry(QRect(10, 300, 231, 181))
        self.input_text_edit = QPlainTextEdit(self.page_1)
        self.input_text_edit.setObjectName(u"input_text_edit")
        self.input_text_edit.setGeometry(QRect(260, 50, 531, 131))
        self.lineEdit = QLineEdit(self.page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 10, 161, 31))
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 200, 51, 31))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_4.setFont(font)
        self.output_text_edit = QTextEdit(self.page_1)
        self.output_text_edit.setObjectName(u"output_text_edit")
        self.output_text_edit.setGeometry(QRect(260, 300, 531, 111))
        self.input_text_edit_2 = QPlainTextEdit(self.page_1)
        self.input_text_edit_2.setObjectName(u"input_text_edit_2")
        self.input_text_edit_2.setGeometry(QRect(310, 200, 481, 31))
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 71, 28))
        self.label_3.setFont(font)
        self.encode = QRadioButton(self.page_1)
        self.encode.setObjectName(u"encode")
        self.encode.setGeometry(QRect(390, 260, 101, 21))
        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 420, 221, 51))
        self.decode = QRadioButton(self.page_1)
        self.decode.setObjectName(u"decode")
        self.decode.setGeometry(QRect(510, 260, 91, 19))
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 250, 131, 41))
        self.label_2.setFont(font)
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 250, 171, 41))
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 10, 49, 31))
        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 270, 41, 21))
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 121, 31))
        self.label.setFont(font)
        self.listWidget_2 = QListWidget(self.page_1)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(30, 180, 181, 81))
        font1 = QFont()
        font1.setPointSize(10)
        self.listWidget_2.setFont(font1)
        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background:lightgreen")
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background:black")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font2 = QFont()
        font2.setPointSize(16)
        self.empty_page_label.setFont(font2)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


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
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

