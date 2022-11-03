from PyQt5.QtWidgets import QItemDelegate, QWidget
from PyQt5 import QtCore
from ...app_settings import SettingsWidget
from py_ballisticcalc.bmath.unit import *
from ...custom_spinbox import CustomDoubleSpinBox


class TwistDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(TwistDelegate, self).__init__(parent)

    def setEditorData(self, editor: CustomDoubleSpinBox, index: QtCore.QModelIndex):
        units = SettingsWidget()
        code = units.twistUnits.currentData()
        suffix = units.twistUnits.currentText()
        raw_value = index.model().data(index, QtCore.Qt.UserRole)
        value = Distance(raw_value, DistanceInch).get_in(code)
        editor.setValue(value) if value else None
        editor.setSuffix(suffix)

    def setModelData(self, editor: CustomDoubleSpinBox, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        units = SettingsWidget()
        code = units.twistUnits.currentData()
        suffix = units.twistUnits.currentText()
        editor.interpretText()
        value = editor.value()
        raw_value = Distance(value, code).get_in(DistanceInch)
        model.setData(index, value, QtCore.Qt.EditRole)
        model.setData(index, raw_value, QtCore.Qt.UserRole)
        model.setData(index, f'{value} {suffix}', QtCore.Qt.DisplayRole)

    def updateEditorGeometry(self, editor: CustomDoubleSpinBox, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        return editor

    # def createEditor(self, parent, option, index):
    #     editor = QtWidgets.QSpinBox(parent)
    #     self.set_props(editor, 0, 10000, 1)
    #     return editor


class SightHeightDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(SightHeightDelegate, self).__init__(parent)

    def setEditorData(self, editor: CustomDoubleSpinBox, index: QtCore.QModelIndex):
        units = SettingsWidget()
        code = units.shUnits.currentData()
        suffix = units.shUnits.currentText()
        raw_value = index.model().data(index, QtCore.Qt.UserRole)
        value = Distance(raw_value, DistanceMillimeter).get_in(code)
        editor.setValue(value) if value else None
        editor.setSuffix(suffix)

    def setModelData(self, editor: CustomDoubleSpinBox, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        units = SettingsWidget()
        code = units.shUnits.currentData()
        suffix = units.shUnits.currentText()
        editor.interpretText()
        value = editor.value()
        raw_value = Distance(value, code).get_in(DistanceMillimeter)
        model.setData(index, value, QtCore.Qt.EditRole)
        model.setData(index, raw_value, QtCore.Qt.UserRole)
        model.setData(index, f'{value} {suffix}', QtCore.Qt.DisplayRole)

    def updateEditorGeometry(self, editor: CustomDoubleSpinBox, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        return editor