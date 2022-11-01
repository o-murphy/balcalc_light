from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidgetItem, QListWidget, QAbstractItemView
from ..abstract_widget import Ui_AbstractWidget
from ..profile_item import ProfileItemWidget
from ..search_bar import SearchBar
from ..abstract_scrollable_list import AbstractScroller


class ProfilesWidget(QWidget, Ui_AbstractWidget):

    def __init__(self, parent=None):
        super(ProfilesWidget, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.search_bar = SearchBar(self)
        self.plist = QListWidget(self)
        self.plist.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scroller = AbstractScroller(self.plist.viewport())
        # self.scroller.setTouchScrollable(True)
        self.scroller.setMouseScrollable(True)

        self.Layout.addWidget(self.search_bar)
        self.Layout.addWidget(self.plist)

        self.set_def_data()  # Todo: temporary

    def set_def_data(self):  # Todo: temporary
        for i in range(20):
            profile = ProfileItemWidget(self)
            profile.rifle_name_text = profile.rifle_name_text + f'_{i}'
            item = QListWidgetItem()
            item.setSizeHint(profile.sizeHint())
            self.plist.addItem(item)
            self.plist.setItemWidget(item, profile)

