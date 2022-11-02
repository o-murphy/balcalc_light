from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView, QScrollArea, QSizePolicy

from ..abstract_centered_label import CenteredHeaderLabel
from ..card_widget import CardWidget
from ..abstract_scrollable_list import AbstractScroller, QScroller


TEMP_RIFLE = {
    'Rifle': "UAR-10",
    'Caliber': '.308 Win',
    'Sight Height': 90,
    'Twist': 10,
}

TEMP_CARTRIDGE = {
    'Cartringe name': "HORNADY 178GR HPBT",
    'Muzzle Velocity': 900,
    'Temperature': 15,
    'Temperature Sens': 1.55,
}

TEMP_BULLET = {
    'Bullet': "HORNADY 178GR HPBT",
    'Weight': 178.0,
    'Length': 1.3,
    'Diameter': 0.308,
    'Drag function mode': 'G7',
    'Drag function data': 0.275
}


class ProfileProps(QScrollArea):
    def __init__(self, parent=None):
        super(ProfileProps, self).__init__(parent)
        # self.setupUi(self)
        self.setWidgetResizable(True)

        self.scroller = AbstractScroller(self.viewport())
        self.scroller.setScrollable(True, QScroller.LeftMouseButtonGesture)
        # self.scroller.setTouchScrollable(True)

        self.Layout = QVBoxLayout(self)

        self.mw = QWidget(self)

        self.mw.Layout = QVBoxLayout(self.mw)
        self.mw.Layout.setContentsMargins(0, 0, 0, 0)
        self.mw.Layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.mw.Layout.setSpacing(0)
        self.mw.resize(200, 1000)

        self.setWidget(self.mw)


        self.rifle_card = CardWidget(self.mw)
        self.cartridge_card = CardWidget(self.mw)
        self.bullet_card = CardWidget(self.mw)

        self.mw.Layout.addWidget(self.rifle_card, 0)
        self.mw.Layout.addWidget(self.cartridge_card, 1)
        self.mw.Layout.addWidget(self.bullet_card, 2)

        self.rifle_label = CenteredHeaderLabel('Rifle', self.rifle_card)
        self.cartridge_label = CenteredHeaderLabel('Cartridge', self.cartridge_card)
        self.bullet_label = CenteredHeaderLabel('Bullet', self.bullet_card)

        self.rifle_table = QTableView(self.rifle_card)
        self.cartridge_table = QTableView(self.cartridge_card)
        self.bullet_table = QTableView(self.bullet_card)

        self.rifle_card.Layout.addWidget(self.rifle_label)
        self.rifle_card.Layout.addWidget(self.rifle_table)
        self.cartridge_card.Layout.addWidget(self.cartridge_label)
        self.cartridge_card.Layout.addWidget(self.cartridge_table)
        self.bullet_card.Layout.addWidget(self.bullet_label)
        self.bullet_card.Layout.addWidget(self.bullet_table)

        self.fill_table(self.rifle_table, TEMP_RIFLE)
        self.fill_table(self.cartridge_table, TEMP_CARTRIDGE)
        self.fill_table(self.bullet_table, TEMP_BULLET)

    def fill_table(self, table, data):
        model = QStandardItemModel(self)
        labels = []
        for k, v in data.items():
            item = QStandardItem()
            item.setData(v, Qt.DisplayRole)
            model.appendRow([item])
            labels.append(k)

        model.setVerticalHeaderLabels(labels)

        table.setModel(model)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().hide()
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setMaximumHeight(table.rowHeight(0) * table.model().rowCount() + 2 + 16)
        table.verticalHeader().setMinimumWidth(120)
