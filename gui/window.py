from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from .template import Ui_MainWindow
from .header import HeaderWidget
from .footer import FooterWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.Layout = QVBoxLayout(self.main_widget)
        self.Layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.header = HeaderWidget(self)
        self.list = QListWidget(self)
        self.footer = FooterWidget(self)

        self.Layout.addWidget(self.header, 0)
        self.Layout.addWidget(self.list, 1)
        self.Layout.addWidget(self.footer, 2)

        self.Layout.setStretch(0, 0)
        self.Layout.setStretch(1, 20)
        self.Layout.setStretch(2, 0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer BC Lite"))

