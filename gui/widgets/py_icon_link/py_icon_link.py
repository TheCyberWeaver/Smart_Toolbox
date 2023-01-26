from qt_core import *
import os
import sys

class PyIconLink(QLabel):
    clicked = Signal(QLabel)
    def __init__(self, parent, lnk_path,
                 bg_color="343b48",
                 width=100,
                 height=100,
                 ):
        super(PyIconLink, self).__init__()
        self.lnk_path = lnk_path
        #self.target = lnk_path
        self.target= lnk_path
        #self.icon = get_icon_from_exe(self.target)
        self.pixmap=QImage("E:\Smarttoolbox\icon.ico")
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

        self.setStyleSheet('PyIconLink{background-color: #c3ccdf; border-radius: 4px;}')

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        exe=self.target
        log = os.system(exe)
        print(log)

        self.clicked.emit()

    def enterEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(True)

    def leaveEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(False)