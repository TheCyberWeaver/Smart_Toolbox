from qt_core import *
import os
import sys
import json
from multiprocessing import Process
import subprocess
class PyIconLink(QLabel):
    #clicked = Signal(QLabel)
    def __init__(self, parent, lnk_path,
                 icon_path="E:\Smarttoolbox\Resources\logo_top_22x22.ico",
                 settings_path="",
                 bg_color="343b48",
                 width=100,
                 height=100,
                 globalAppListSavePath=""
                 ):
        super(PyIconLink, self).__init__()
        self.lnk_path = lnk_path
        self.settingsPath=settings_path
        #self.target = lnk_path
        self.linkTarget= lnk_path
        self.globalAppListSavePath=globalAppListSavePath

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
        action.triggered.connect(self.rightClickOpenLink)

        action1 = menu.addAction("properties")
        action1.triggered.connect(self.showProperties)


        action2 = menu.addAction("delete")
        action2.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

    def delete(self):
        print("[Info][py_icon_link]:delete")

        with open(self.globalAppListSavePath, "r", encoding='utf-8') as reader:
            list = json.loads(reader.read())
            list.remove(self.settingsPath)
        with open(self.globalAppListSavePath, "w", encoding='utf-8') as write:
            json.dump(list, write, indent=4)

        self.deleteLater()

    def showProperties(self):
        print("[Info][py_icon_link]:showing properties using default editor")
        subprocess.Popen(['C:\\Windows\\notepad.exe', self.settingsPath])
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.buttons()==Qt.LeftButton:
            self.openLink(self.linkTarget)
        else:
            pass
    def rightClickOpenLink(self):
        self.openLink(self.linkTarget)
    def openLink(self,target):
        exe = target
        # log = os.system(exe)
        # print(log)
        try:
            string="cd "+self.settingsPath[:-13]
            print(string)
            #os.system(string)
            #os.system(exe)
            #p = Process(target=os.system, args=(exe,)) #使用pocess打包后会出现奇怪的问题，打开程序会打开smarttoolbox本身
            #p.start()

            os.startfile(exe)
            print("[Info][py_icon_link]:starting application: <"+exe+">")
        except:
            print("[Failed][py_icon_link]:could not start application: <"+exe+">")
    def enterEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(True)

    def leaveEvent(self, a0: QEvent) -> None:
        self.graphicsEffect().setEnabled(False)