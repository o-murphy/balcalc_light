from PyQt5.QtWidgets import QTabWidget
from ..profiles import ProfilesWidget


class TabsWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabsWidget, self).__init__(parent)

        self.tabBar().setVisible(False)

        self.profiles = ProfilesWidget(self)
        self.settings = None  # Todo: add tab

        self.addTab(self.profiles, 'Profiles')

