from qt_core import *
import os
import sys

class PyWalletButton(QLabel):
    #clicked = Signal(QLabel)
    def __init__(self,parent,
                 icon_path="E:\Smarttoolbox\Resources\logo_top_22x22.ico",
                 bg_color="343b48",
                 wallet_name="",

                 width=75,
                 height=75,
                 ):
        super(PyWalletButton, self).__init__()
        self.parent=parent
        #self.icon = get_icon_from_exe(self.target)
        self.pixmap=QImage(icon_path)
        self.fitPixmap = self.pixmap.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(QPixmap(self.fitPixmap))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(width, height)
        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(7)
        self.shadow.setYOffset(7)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.shadow.setEnabled(False)
        self.setGraphicsEffect(self.shadow)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        self.setStyleSheet('PyWalletButton{background-color: #c3ccdf; border-radius: 4px;}')

        #Data

        self.name=wallet_name

    def show_context_menu(self, pos):
        menu = QMenu(self)
        #menu.setStyleSheet("QMenu {background-color: #FFFAFA;border-color: #00000F;}")

        action1 = menu.addAction("properties")
        action1.triggered.connect(self.showProperties)


        action2 = menu.addAction("delete")
        action2.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

    def delete(self):
        print("delete")
        self.parent.ui.gridLayout.removeWidget(self)

    def showProperties(self):
        print("show properties")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.buttons()==Qt.LeftButton:
            pass
        else:
            pass


    def enterEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(True)

    def leaveEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(False)