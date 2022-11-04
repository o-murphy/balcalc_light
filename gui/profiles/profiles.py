from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ..abstract_widget import Ui_AbstractWidget
from ..search_bar import SearchBar
from .profile_list import ProfilesList


class ProfilesWidget(QWidget, Ui_AbstractWidget):

    def __init__(self, parent=None):
        super(ProfilesWidget, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.search_bar = SearchBar(self)
        self.plist = ProfilesList(self)

        self.Layout.addWidget(self.search_bar)
        self.Layout.addWidget(self.plist)
