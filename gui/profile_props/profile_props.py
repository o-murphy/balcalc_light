from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView, QScrollArea, QSizePolicy, QGridLayout

from ..abstract_centered_label import CenteredHeaderLabel
from ..card_widget import CardWidget
from ..abstract_scrollable_list import AbstractScroller, QScroller
from .props_delegates import *
from py_ballisticcalc.bmath.unit import *


TEMP_RIFLE = {
    'Rifle': "UAR-10",
    'Caliber': '.308 Win',
    'Sight Height': 90.0,
    'Twist': 10.0,
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

TEMP_CONDITIONS = {
    'Temp': 15,
    'PowderTemp': 15,
    'Pressure': 760,
    'Humidity': 50,
    'Latitude': 0,
    'Angle': 0,
    'Azimuth': 0,
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

        self.mw.Layout = QGridLayout(self.mw)
        self.mw.Layout.setContentsMargins(0, 0, 0, 0)
        self.mw.Layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.mw.Layout.setSpacing(0)
        # self.mw.resize(200, 1000)

        self.setWidget(self.mw)

        self.rifle_card = CardWidget(self.mw)
        self.cartridge_card = CardWidget(self.mw)
        self.bullet_card = CardWidget(self.mw)
        self.conditions_card = CardWidget(self.mw)

        self.mw.Layout.addWidget(self.rifle_card)
        self.mw.Layout.addWidget(self.cartridge_card)
        self.mw.Layout.addWidget(self.bullet_card)
        self.mw.Layout.addWidget(self.conditions_card)

        self.rifle_label = CenteredHeaderLabel('Rifle', self.rifle_card)
        self.cartridge_label = CenteredHeaderLabel('Cartridge', self.cartridge_card)
        self.bullet_label = CenteredHeaderLabel('Bullet', self.bullet_card)
        self.conditions_label = CenteredHeaderLabel('Conditions', self.bullet_card)

        self.rifle_table = QTableView(self.rifle_card)
        self.cartridge_table = QTableView(self.cartridge_card)
        self.bullet_table = QTableView(self.bullet_card)
        self.conditions_table = QTableView(self.bullet_card)

        self.rifle_table.setEditTriggers(QTableView.SelectedClicked | QTableView.CurrentChanged)
        self.cartridge_table.setEditTriggers(QTableView.SelectedClicked | QTableView.CurrentChanged)
        self.bullet_table.setEditTriggers(QTableView.SelectedClicked | QTableView.CurrentChanged)
        self.conditions_table.setEditTriggers(QTableView.SelectedClicked | QTableView.CurrentChanged)

        self.rifle_table.setSelectionMode(QTableView.SingleSelection)
        self.cartridge_table.setSelectionMode(QTableView.SingleSelection)
        self.bullet_table.setSelectionMode(QTableView.SingleSelection)
        self.conditions_table.setSelectionMode(QTableView.SingleSelection)

        self.rifle_card.Layout.addWidget(self.rifle_label)
        self.rifle_card.Layout.addWidget(self.rifle_table)
        self.cartridge_card.Layout.addWidget(self.cartridge_label)
        self.cartridge_card.Layout.addWidget(self.cartridge_table)
        self.bullet_card.Layout.addWidget(self.bullet_label)
        self.bullet_card.Layout.addWidget(self.bullet_table)
        self.conditions_card.Layout.addWidget(self.conditions_label)
        self.conditions_card.Layout.addWidget(self.conditions_table)

        self.rifle_table.setItemDelegateForRow(2, SightHeightDelegate(self.rifle_table))
        self.rifle_table.setItemDelegateForRow(3, TwistDelegate(self.rifle_table))

        self.fill_table(self.rifle_table, TEMP_RIFLE)
        self.fill_table(self.cartridge_table, TEMP_CARTRIDGE)
        self.fill_table(self.bullet_table, TEMP_BULLET)
        self.fill_table(self.conditions_table, TEMP_CONDITIONS)


    def fill_table(self, table: QTableView, data):
        model = QStandardItemModel(self)
        labels = []
        for k, v in data.items():
            item = QStandardItem()
            item.setData(v, Qt.DisplayRole)
            item.setData(v, Qt.UserRole)
            item.setTextAlignment(Qt.AlignCenter)
            model.appendRow([item])
            labels.append(k)

        model.setVerticalHeaderLabels(labels)

        table.setModel(model)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().hide()
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table_height = (table.rowHeight(0) + 1) * table.model().rowCount() + 2 + 8
        table.setMaximumHeight(table_height)
        table.setMinimumHeight(table_height)
        table.verticalHeader().setMinimumWidth(120)
