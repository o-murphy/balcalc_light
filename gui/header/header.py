from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QCoreApplication
from .template import Ui_Header


class HeaderWidget(QWidget, Ui_Header):
    def __init__(self, parent=None):
        super(HeaderWidget, self).__init__(parent)
        self.setupUi(self)

    def retranslateUi(self, Header):
        _translate = QCoreApplication.translate
        Header.setWindowTitle(_translate("Header", "Form"))
        self.app_title.setText(_translate("Header", "Archer BC Lite"))
