from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from ..abstract_widget import Ui_AbstractWidget


class FooterWidget(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(FooterWidget, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QHBoxLayout(self)

        self.profiles_btn = QPushButton('Profiles', self)
        self.settings_btn = QPushButton('Settings', self)

        self.Layout.addWidget(self.profiles_btn, 0)
        self.Layout.addWidget(self.settings_btn, 1)

        self.Layout.setStretch(0, 0)
        self.Layout.setStretch(1, 0)
