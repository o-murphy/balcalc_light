from ..props_table_view import PropsTableView
from ..props_delegates import VelocityDelegate, TemperatureDelegate
from ...abstract_centered_label import CenteredHeaderLabel
from ...card_widget import CardWidget


class CartridgeProps(PropsTableView):
    def __init__(self, parent=None):
        super(CartridgeProps, self).__init__(parent)

        self.setItemDelegateForRow(1, VelocityDelegate(self))
        self.setItemDelegateForRow(2, TemperatureDelegate(self))


class CartridgeCard(CardWidget):
    def __init__(self, parent=None):
        super(CartridgeCard, self).__init__(parent)

        self.label = CenteredHeaderLabel('Cartridge', self)
        self.table = CartridgeProps(self)

        self.Layout.addWidget(self.label)
        self.Layout.addWidget(self.table)

