from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QGroupBox, QSizePolicy


class CardWidget(QFrame):
    def __init__(self, parent=None):
        super(CardWidget, self).__init__(parent)
        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(0)
        self.Layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
