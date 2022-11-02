from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


class CenteredHeaderLabel(QLabel):
    def __init__(self, text: str, parent=None):
        super(CenteredHeaderLabel, self).__init__(text, parent)

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
