from ..props_table_view import PropsTableView
from ..props_delegates import *
from ...abstract_centered_label import CenteredHeaderLabel
from ...card_widget import CardWidget


class ConditionsProps(PropsTableView):
    def __init__(self, parent=None):
        super(ConditionsProps, self).__init__(parent)


class ConditionsCard(CardWidget):
    def __init__(self, parent=None):
        super(ConditionsCard, self).__init__(parent)

        self.label = CenteredHeaderLabel('Conditions', self)
        self.table = ConditionsProps(self)

        self.Layout.addWidget(self.label)
        self.Layout.addWidget(self.table)

