from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import pyqtSignal


class ProfileListContextMenu(QMenu):
    newActSignal = pyqtSignal()
    copyActSignal = pyqtSignal()
    delActSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(ProfileListContextMenu, self).__init__(parent)
        self.new_action = QAction('New', self)
        self.copy_action = QAction('Make Copy', self)
        self.delete_action = QAction('Delete', self)

        self.addAction(self.new_action)
        self.addAction(self.copy_action)
        self.addAction(self.delete_action)

        self.new_action.triggered.connect(self._new_trigger)
        self.copy_action.triggered.connect(self._copy_trigger)
        self.delete_action.triggered.connect(self._del_trigger)

    def _new_trigger(self):
        self.newActSignal.emit()

    def _copy_trigger(self):
        self.copyActSignal.emit()

    def _del_trigger(self):
        self.delActSignal.emit()

