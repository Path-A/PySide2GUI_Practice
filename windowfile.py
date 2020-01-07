from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QIcon, QPixmap
from PySide2 import QtCore

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside Simple Application")
        self.setGeometry(300, 300, 300, 300)
        self.setMinimumHeight(100)
        self.setMinimumWidth(150)
        self.setMaximumHeight(500)
        self.setMaximumWidth(800)

        self.setIcon()
        self.setIconModes()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)

        # Second Icon
        icon2 = QIcon("icon.png")
        label2 = QLabel("sample", self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)

        # Third
        icon3 = QIcon("icon.png")
        label3 = QLabel("sample", self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    myApp = QApplication(sys.argv)

    window = Window()
    window.show()

    myApp.exec_()
    sys.exit(0)
