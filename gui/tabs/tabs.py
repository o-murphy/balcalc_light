from PyQt5.QtWidgets import QTabWidget
from ..profiles import ProfilesWidget
from ..profile_props import ProfileProps
from ..app_settings import SettingsWidget
from ..fader_tabs import FaderTabWidget


class TabsWidget(FaderTabWidget):
    def __init__(self, parent=None):
        super(TabsWidget, self).__init__(parent)

        self.setTabPosition(self.TabPosition.South)
        self.tabBar().setDocumentMode(True)
        self.tabBar().setExpanding(True)

        self.profiles = ProfilesWidget(self)
        self.profile_props = ProfileProps(self)
        self.settings = SettingsWidget(self)

        self.addTab(self.profiles, 'Profiles')
        self.addTab(self.profile_props, 'Props')
        self.addTab(self.settings, 'Settings')

