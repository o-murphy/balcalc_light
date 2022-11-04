from ..props_table_view import PropsTableView
from ..props_delegates import SightHeightDelegate, TwistDelegate
from ...abstract_centered_label import CenteredHeaderLabel
from ...card_widget import CardWidget


class RifleProps(PropsTableView):
    def __init__(self, parent=None):
        super(RifleProps, self).__init__(parent)

        self.setItemDelegateForRow(2, SightHeightDelegate(self))
        self.setItemDelegateForRow(3, TwistDelegate(self))


class RifleCard(CardWidget):
    def __init__(self, parent=None):
        super(RifleCard, self).__init__(parent)

        self.label = CenteredHeaderLabel('Rifle', self)
        self.table = RifleProps(self)

        self.Layout.addWidget(self.label)
        self.Layout.addWidget(self.table)

