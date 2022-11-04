from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QScroller, QListWidgetItem

from ...abstract_scrollable_list import AbstractScroller
from ..profile_item import ProfileItemWidget
from ..profile_list_context_menu import ProfileListContextMenu


class ProfilesList(QListWidget):
    def __init__(self, parent=None):
        super(ProfilesList, self).__init__(parent)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.scroller = AbstractScroller(self.viewport())
        self.scroller.setScrollable(True, QScroller.LeftMouseButtonGesture)
        self.installEventFilter(self)

        self._set_def_data()  # Todo: temporary

        self.context_menu = ProfileListContextMenu(self)
        self.context_menu.newActSignal.connect(self.new_item)
        self.context_menu.delActSignal.connect(self.del_item)
        self.context_menu.copyActSignal.connect(self.copy_item)

        self.menu_action_item: QListWidgetItem = None

    def new_item(self):
        self._add_row()

    def del_item(self):
        self._rm_row()

    def copy_item(self):
        self._cp_row()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self:
            self.menu_action_item = source.itemAt(event.pos())
            self.context_menu.exec_(event.globalPos())
            # if action:
            #     item: QListWidgetItem = source.itemAt(event.pos())
            #     widget: ProfileItemWidget = source.itemWidget(item)
            #     print(widget.rifle_name_text, widget.database_id, action.text())  # Todo: dbworker funcs
            # return True
        return super(ProfilesList, self).eventFilter(source, event)

    def _rm_row(self):
        self.takeItem(self.row(self.menu_action_item))

    def _cp_row(self):
        item_copy = self.menu_action_item.clone()
        widget = self.itemWidget(self.menu_action_item)
        widget_copy = widget.__new__(ProfileItemWidget)
        self.addItem(item_copy)
        self.setItemWidget(widget_copy)

        # item_copy = QListWidgetItem(self.menu_action_item)
        # widget_copy = self.itemWidget(self.menu_action_item)
        # self.item().c
        # QListWidgetItem
        # self.addItem(item_copy)
        # self.setItemWidget(item_copy, widget_copy)

    def _add_row(self):
        i = self.count()
        profile = ProfileItemWidget(self, database_id=i)
        profile.rifle_name_text = profile.rifle_name_text + f'_{i}'
        item = QListWidgetItem()
        item.setSizeHint(profile.sizeHint())
        self.addItem(item)
        self.setItemWidget(item, profile)

    def _set_def_data(self):  # Todo: temporary
        for i in range(20):
            self._add_row()

