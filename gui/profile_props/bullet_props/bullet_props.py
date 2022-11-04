from ..props_table_view import PropsTableView
from ..props_delegates import *
from ...abstract_centered_label import CenteredHeaderLabel
from ...card_widget import CardWidget


class BulletProps(PropsTableView):
    def __init__(self, parent=None):
        super(BulletProps, self).__init__(parent)


class BulletCard(CardWidget):
    def __init__(self, parent=None):
        super(BulletCard, self).__init__(parent)

        self.label = CenteredHeaderLabel('Bullet', self)
        self.table = BulletProps(self)

        self.Layout.addWidget(self.label)
        self.Layout.addWidget(self.table)

