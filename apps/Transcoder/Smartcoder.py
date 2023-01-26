# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Smartcoder.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QWidget)
from Resources import pic_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(807, 486)
        self.input_text_edit = QPlainTextEdit(Dialog)
        self.input_text_edit.setObjectName(u"input_text_edit")
        self.input_text_edit.setGeometry(QRect(260, 50, 531, 131))
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 420, 221, 51))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 10, 161, 31))
        self.encode = QRadioButton(Dialog)
        self.encode.setObjectName(u"encode")
        self.encode.setGeometry(QRect(380, 260, 61, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 61, 28))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 430, 301, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 91, 31))
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 181, 111))
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.decode = QRadioButton(Dialog)
        self.decode.setObjectName(u"decode")
        self.decode.setGeometry(QRect(470, 260, 71, 19))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 270, 41, 21))
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.AutoText)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 250, 211, 41))
        self.input_text_edit_2 = QPlainTextEdit(Dialog)
        self.input_text_edit_2.setObjectName(u"input_text_edit_2")
        self.input_text_edit_2.setGeometry(QRect(310, 200, 481, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 240, 101, 41))
        self.label_2.setFont(font1)
        self.output_text_edit_2 = QTextEdit(Dialog)
        self.output_text_edit_2.setObjectName(u"output_text_edit_2")
        self.output_text_edit_2.setGeometry(QRect(10, 300, 231, 171))
        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(10, 180, 181, 81))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 20, 49, 21))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 200, 41, 31))
        self.label_4.setFont(font1)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 811, 491))
        self.label_7.setPixmap(QPixmap(u":/newPrefix/R.jpg"))
        self.label_7.setScaledContents(True)
        self.output_text_edit = QTextEdit(Dialog)
        self.output_text_edit.setObjectName(u"output_text_edit")
        self.output_text_edit.setGeometry(QRect(260, 300, 531, 111))
        self.ClearButton = QPushButton(Dialog)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(220, 10, 21, 31))
        self.label_7.raise_()
        self.input_text_edit.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.encode.raise_()
        self.label_3.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.listWidget.raise_()
        self.decode.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.input_text_edit_2.raise_()
        self.label_2.raise_()
        self.output_text_edit_2.raise_()
        self.listWidget_2.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.output_text_edit.raise_()
        self.ClearButton.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.input_text_edit.setPlainText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Smart Conversion (beta)", None))
        self.encode.setText(QCoreApplication.translate("Dialog", u"Encode", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Declaration", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Input Text", None))
        self.decode.setText(QCoreApplication.translate("Dialog", u"Decode", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Info", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Convert", None))
        self.input_text_edit_2.setPlainText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Output Text", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Using:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Key", None))
        self.label_7.setText("")
        self.ClearButton.setText(QCoreApplication.translate("Dialog", u"X", None))
    # retranslateUi

