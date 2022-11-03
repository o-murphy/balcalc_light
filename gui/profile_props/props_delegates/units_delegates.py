from PyQt5.QtWidgets import QItemDelegate, QWidget
from PyQt5 import QtCore
from ...app_settings import SettingsWidget
from py_ballisticcalc.bmath.unit import *
from ...custom_spinbox import CustomDoubleSpinBox


class DoubleSpinBoxDelegate(QItemDelegate):

    def set_props(self, editor, min, max, step, dec=None):
        editor.setMaximum(max)
        editor.setMinimum(min)
        editor.setSingleStep(step)
        if dec:
            editor.setDecimals(dec)
        return editor

    def updateEditorGeometry(self, editor: CustomDoubleSpinBox, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)


class TwistDelegate(DoubleSpinBoxDelegate):

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

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        self.set_props(editor, 0, 30, 0.1)
        return editor


class SightHeightDelegate(DoubleSpinBoxDelegate):

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

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        self.set_props(editor, 0, 1000, 0.1)
        return editor


class VelocityDelegate(DoubleSpinBoxDelegate):

    def setEditorData(self, editor: CustomDoubleSpinBox, index: QtCore.QModelIndex):
        units = SettingsWidget()
        code = units.vUnits.currentData()
        suffix = units.vUnits.currentText()
        raw_value = index.model().data(index, QtCore.Qt.UserRole)
        value = Velocity(raw_value, VelocityMPS).get_in(code)
        editor.setValue(value) if value else None
        editor.setSuffix(suffix)

    def setModelData(self, editor: CustomDoubleSpinBox, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        units = SettingsWidget()
        code = units.vUnits.currentData()
        suffix = units.vUnits.currentText()
        editor.interpretText()
        value = editor.value()
        raw_value = Velocity(value, code).get_in(VelocityMPS)
        model.setData(index, value, QtCore.Qt.EditRole)
        model.setData(index, raw_value, QtCore.Qt.UserRole)
        model.setData(index, f'{value} {suffix}', QtCore.Qt.DisplayRole)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        self.set_props(editor, 0, 10000, 1)
        return editor


class TemperatureDelegate(DoubleSpinBoxDelegate):

    def setEditorData(self, editor: CustomDoubleSpinBox, index: QtCore.QModelIndex):
        units = SettingsWidget()
        code = units.tempUnits.currentData()
        suffix = units.tempUnits.currentText()
        raw_value = index.model().data(index, QtCore.Qt.UserRole)
        value = Temperature(raw_value, TemperatureCelsius).get_in(code)
        editor.setValue(value) if value else None
        editor.setSuffix(suffix)

    def setModelData(self, editor: CustomDoubleSpinBox, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        units = SettingsWidget()
        code = units.tempUnits.currentData()
        suffix = units.tempUnits.currentText()
        editor.interpretText()
        value = editor.value()
        raw_value = Temperature(value, code).get_in(TemperatureCelsius)
        model.setData(index, value, QtCore.Qt.EditRole)
        model.setData(index, raw_value, QtCore.Qt.UserRole)
        model.setData(index, f'{value} {suffix}', QtCore.Qt.DisplayRole)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = CustomDoubleSpinBox(parent)
        self.set_props(editor, 0, 10000, 1)
        return editor