from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from ..abstract_widget import Ui_AbstractWidget


class ProfileItemWidget(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(ProfileItemWidget, self).__init__(parent)

        self.Layout = QGridLayout(self)

        self._pix = QPixmap(24, 24)
        self._pix.fill(Qt.white)
        self._pix_label = QLabel(self)
        self._pix_label.setPixmap(self._pix)

        self._rifle_name = QLabel('rifle', self)
        self._cartridge_name = QLabel('cart', self)
        self._caliber_name = QLabel('cal', self)
        self._bullet_weight = QLabel('0', self)

        self.Layout.addWidget(self._pix_label, 0, 0, 2, 1)
        self.Layout.addWidget(self._rifle_name, 0, 1)
        self.Layout.addWidget(self._cartridge_name, 1, 1)
        self.Layout.addWidget(self._caliber_name, 0, 2)
        self.Layout.addWidget(self._bullet_weight, 1, 2)

        self.Layout.setColumnStretch(0, 0)
        self.Layout.setColumnStretch(1, 1)
        self.Layout.setColumnStretch(2, 1)

    @property
    def rifle_name_text(self):
        return self._rifle_name.text()

    @rifle_name_text.setter
    def rifle_name_text(self, text: str):
        self._rifle_name.setText(text)

