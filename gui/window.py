from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore
from .template import Ui_MainWindow
from .header import HeaderWidget
from .tabs import TabsWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    configChanged = pyqtSignal(object)

    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.Layout = QVBoxLayout(self.main_widget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.header = HeaderWidget(self)
        self.tabs = TabsWidget(self)

        self.Layout.addWidget(self.header, 0)
        self.Layout.addWidget(self.tabs, 1)

        self.Layout.setStretch(0, 0)
        self.Layout.setStretch(1, 20)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer BC Lite"))

