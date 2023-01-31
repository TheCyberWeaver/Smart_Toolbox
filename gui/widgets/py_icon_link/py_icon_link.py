from qt_core import *
import os
import sys
from multiprocessing import Process
class PyIconLink(QLabel):
    #clicked = Signal(QLabel)
    def __init__(self, parent, lnk_path,
                 icon_path="E:\Smarttoolbox\Resources\logo_top_22x22.ico",
                 bg_color="343b48",
                 width=100,
                 height=100,
                 ):
        super(PyIconLink, self).__init__()
        self.lnk_path = lnk_path
        #self.target = lnk_path
        self.target= lnk_path

        #self.icon = get_icon_from_exe(self.target)
        self.pixmap=QImage(icon_path)
        self.fitPixmap = self.pixmap.scaled(75, 75, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
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

        self.setStyleSheet('PyIconLink{background-color: #c3ccdf; border-radius: 4px;}')

    def show_context_menu(self, pos):
        menu = QMenu(self)
        #menu.setStyleSheet("QMenu {background-color: #FFFAFA;border-color: #00000F;}")

        action = menu.addAction("Open")
        action.triggered.connect(self.openLink)

        action1 = menu.addAction("properties")
        action1.triggered.connect(self.showProperties)


        action2 = menu.addAction("delete")
        action2.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

    def delete(self):
        print("delete")

    def showProperties(self):
        print("show properties")
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.buttons()==Qt.LeftButton:
            self.openLink()
        else:
            pass
    def openLink(self):
        exe = self.target
        # log = os.system(exe)
        # print(log)
        p = Process(target=os.system, args=(exe,))
        p.start()
    def enterEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(True)

    def leaveEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(False)