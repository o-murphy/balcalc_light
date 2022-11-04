from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore
from .template import Ui_MainWindow
from .header import HeaderWidget
from .tabs import TabsWidget
from .profile_props import ProfileProps
from enum import IntFlag, auto


class Orientation(IntFlag):
    vertical = auto()
    horizontal = auto()


class MainWindow(QMainWindow, Ui_MainWindow):
    configChanged = pyqtSignal(object)

    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.orientation = Orientation.vertical
        self.setupUi(self)

        self.tabs.profiles.plist.itemClicked.connect(self.open_props)
        self.props.hide()

    def open_props(self, item):
        self.props.raise_()
        self.props.show()

    def keyPressEvent(self, a0: 'QKeyEvent') -> None:
        super(MainWindow, self).keyPressEvent(a0)
        if a0.key() == (Qt.Key_Escape or Qt.Key_Back):
            self.tabs.raise_()
            self.props.hide()

    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.Layout = QGridLayout(self.main_widget)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.header = HeaderWidget(self)
        self.tabs = TabsWidget(self)
        self.props = ProfileProps(self)

        # self.Layout.addWidget(self.header, 0, 0, 1, 1)
        # self.Layout.addWidget(self.tabs, 0, 1, 1, 1)

        self.Layout.setColumnStretch(1, 2)
        self.Layout.setRowStretch(1, 20)

    def resizeEvent(self, a0: 'QResizeEvent') -> None:
        super(MainWindow, self).resizeEvent(a0)
        size = self.size()
        if size.width() > size.height():
            self.orientation = Orientation.horizontal
            self.Layout.addWidget(self.header, 0, 0, 1, 2)
            self.Layout.addWidget(self.props, 1, 1, 1, 1)
            self.Layout.addWidget(self.tabs, 1, 0, 1, 1)
            # self.tabs.setTabPosition(self.tabs.TabPosition.West)
            # self.tabs.tabBar().setExpanding(False)
        else:
            self.orientation = Orientation.vertical
            self.Layout.addWidget(self.header, 0, 0, 1, 2)
            self.Layout.addWidget(self.props, 1, 0, 1, 2)
            self.Layout.addWidget(self.tabs, 1, 0, 1, 2)
            # self.tabs.setTabPosition(self.tabs.TabPosition.South)
            # self.tabs.tabBar().setExpanding(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archer BC Lite"))

