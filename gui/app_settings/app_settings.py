from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ..abstract_widget import Ui_AbstractWidget
from modules import Units
from py_ballisticcalc.bmath import unit


class SettingsWidget(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)


    def setupUi(self, AbstractWidget):
        super(SettingsWidget, self).setupUi(self)
