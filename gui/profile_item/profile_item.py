from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ..abstract_widget import Ui_AbstractWidget


class ProfileItemWidget(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(ProfileItemWidget, self).__init__(parent)

        self.Layout = QGridLayout(self)

        self._img = QPixmap('resources/circle.svg')
        self._icon = QLabel(self)
        self._icon.setPixmap(self._img)

        self._rifle_name = QLabel('Accuracy International', self)
        self._cartridge_name = QLabel('Ukrop', self)
        self._caliber_name = QLabel('338LM', self)
        self._bullet_weight = QLabel('250GR', self)

        self.Layout.addWidget(self._icon, 0, 0, 2, 1)
        self.Layout.addWidget(self._caliber_name, 0, 1)
        self.Layout.addWidget(self._bullet_weight, 1, 1)
        self.Layout.addWidget(self._rifle_name, 0, 2)
        self.Layout.addWidget(self._cartridge_name, 1, 2)

        self.Layout.setColumnStretch(0, 0)
        self.Layout.setColumnStretch(1, 0)
        self.Layout.setColumnStretch(2, 1)

    @property
    def rifle_name_text(self):
        return self._rifle_name.text()

    @rifle_name_text.setter
    def rifle_name_text(self, text: str):
        self._rifle_name.setText(text)

