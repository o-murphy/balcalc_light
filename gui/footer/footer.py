from PyQt5.QtWidgets import QWidget
from .template import Ui_Footer


class FooterWidget(QWidget, Ui_Footer):
    def __init__(self, parent=None):
        super(FooterWidget, self).__init__(parent)
        self.setupUi(self)
