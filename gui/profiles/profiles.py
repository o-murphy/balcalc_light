from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QListWidgetItem
from ..abstract_widget import Ui_AbstractWidget
from ..profile_item import ProfileItemWidget


class ProfilesWidget(QWidget, Ui_AbstractWidget):
    def __init__(self, parent=None):
        super(ProfilesWidget, self).__init__(parent)
        self.setupUi(self)

        self.Layout = QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.plist = QListWidget(self)

        self.Layout.addWidget(self.plist)

        self.set_def_data()  # Todo: temporary

    def set_def_data(self):  # Todo: temporary
        for i in range(15):
            profile = ProfileItemWidget(self)
            profile.rifle_name_text = f'rifle{i}'
            item = QListWidgetItem()
            item.setSizeHint(profile.sizeHint())
            self.plist.addItem(item)
            self.plist.setItemWidget(item, profile)

