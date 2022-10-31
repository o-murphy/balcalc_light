from PyQt5.QtWidgets import QWidget
from .template import Ui_Header


class HeaderWidget(QWidget, Ui_Header):
    def __init__(self, parent=None):
        super(HeaderWidget, self).__init__(parent)
        self.setupUi(self)
