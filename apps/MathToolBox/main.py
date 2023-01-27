# coding:utf-8
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

# IMPORT QT CORE
from qt_core import *

from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
from gui.core.json_settings import Settings

import sys
import numpy as np
#from readonly.HeightsModule import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from ui_MathToolBox import Ui_Form
from setup_ui import SetupMainWindow
#An Example of ploting graphs in pyside6
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

#An Example of ploting graphs in pyside6
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        self.show()

class MathToolBox(QWidget):

    def __init__(self):
        super().__init__()
        self.settingFilesFolderPath = "apps\PasswordManager"

        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        settings = Settings(self.settingFilesFolderPath)
        print("[info]: using", settings.settings_path)
        self.settings = settings.items
        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        # self.hide_grips = True  # Show/Hide resize grips

        SetupMainWindow.setup_gui(self)

        self.uiInitiation()

    def uiInitiation(self):
        self.push_button_4.clicked.connect(lambda: self.vectorfieldShow())

    def vectorfieldShow(self):


        x_intervalMin=int(self.line_edit_3.text())
        x_intervalMax=int(self.line_edit_4.text())

        y_intervalMin=int(self.line_edit_5.text())
        y_intervalMax=int(self.line_edit_6.text())

        self.function_u_expression=self.line_edit.text()
        self.function_v_expression = self.line_edit_2.text()

        X,Y=np.mgrid[x_intervalMin:x_intervalMax, y_intervalMin:y_intervalMax]
        Vector_X=[]
        Vector_Y=[]
        for x in range(x_intervalMin,x_intervalMax):
            Vector_X.append([self.function_u(x,y) for y in range(y_intervalMin,y_intervalMax)])
        for x in range(x_intervalMin,x_intervalMax):
            Vector_Y.append([self.function_v(x,y) for y in range(y_intervalMin,y_intervalMax)])


        plt.quiver(X, Y,Vector_X,Vector_Y)

        plt.show()
    def function_u(self,x,y):
        try:
            return eval(self.function_u_expression)
        except:
            return 0

    def function_v(self,x,y):
        try:
            return eval(self.function_v_expression)
        except:
            return 0
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MathToolBox()
    print("[info]: Process", window.settings["app_name"], "is starting")
    window.show()

    sys.exit(app.exec())