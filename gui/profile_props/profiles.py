from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView
from ..abstract_widget import Ui_AbstractWidget


class ProfileProps(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(ProfileProps, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.table = QTableView(self)

        self.Layout.addWidget(self.table)



