from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ..abstract_widget import Ui_AbstractWidget
from modules import Units
from py_ballisticcalc.bmath import unit

from configparser import ConfigParser
import os
from pathlib import Path

from PyQt5.QtCore import QCoreApplication, QLocale, Qt
from PyQt5.QtWidgets import QDialog, QComboBox, QCheckBox

from .template import Ui_AppSettings
from py_ballisticcalc.bmath.unit import *


CONFIG_PATH = 'config.ini'

# class SettingsWidget(QWidget, Ui_AbstractWidget):
#     def __init__(self, parent=None):
#         super(SettingsWidget, self).__init__(parent)
#         self.setupUi(self)
#
#         self.Layout = QVBoxLayout(self)
#         self.Layout.setContentsMargins(0, 0, 0, 0)
#
#
#     def setupUi(self, AbstractWidget):
#         super(SettingsWidget, self).setupUi(self)
#
#
# # -*u.- coding: utf-8 -*u.-




# loads, writes and sets app preferences from settings.ini file
class SettingsWidget(QWidget, Ui_AppSettings):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.setupUi(self)

        self.config = ConfigParser()
        self.config.read(CONFIG_PATH)

        # recreate settings.ini if it's format wrong
        try:
            self.update_config()
        except Exception:
            os.remove(CONFIG_PATH)
            self.update_config()

    def update_config(self):
        """loads all settings to current widget"""
        # self.init_general_tab()
        self.init_units_tab()

        # self.load_general_settings()
        self.load_unit_settings()

        # self.init_extension_tab()
        # self.load_extension_settings()

        self.save_cfg()

    def save_cfg(self):
        with open(CONFIG_PATH, 'w') as fp:
            self.config.write(fp)

    def init_general_tab(self):
        """creates general settings tab, loads settings or sets it to default values"""
        self.languages = ['en', 'ua', 'ru']
        for i, lang in enumerate(self.languages):
            self.Language.setItemData(i, lang)

        if 'General' not in self.config:
            self.config.add_section('General')
            self.config.set('General', 'exp_dfed', '0')
        self.xdfed.setChecked(self.config.getboolean('General', 'exp_dfed'))


    def init_extension_tab(self):
        """creates extension settings tab, loads settings or sets it to default values"""

        root = Path(__file__).parent.parent
        edir = Path(root, 'extensions')
        if not os.path.exists(edir):
            return

        if 'Extensions' not in self.config:
            self.config.add_section('Extensions')

        for each in edir.iterdir():
            if each.is_dir() and not str(each.name).startswith('__'):
                ext_name = f'extensions.{each.name}'
                if ext_name not in self.config['Extensions']:
                    self.config.set('Extensions', ext_name, str(True))

    def load_extension_settings(self):
        """loads which extensions are enabled"""
        root = Path(__file__).parent.parent
        edir = Path(root, 'extensions')
        if not os.path.exists(edir):
            return

        layout = self.tabExtensions.layout()
        layout.setAlignment(Qt.AlignTop)

        for i, (k, v) in enumerate(self.config['Extensions'].items()):
            text = k.replace('extensions.', '').replace('_', ' ').capitalize()
            cb = QCheckBox()
            cb.setText(text)
            cb.setObjectName(k)
            is_checked = self.config['Extensions'].getboolean(k)
            cb.setChecked(is_checked)
            layout.addWidget(cb, i, 0, 1, 1)

    def init_units_tab(self):
        """
        creates extension _cur_units tab, loads settings or sets it to default values
        that will be used globally in the app and a ballistics calculations
        """

        u = self

        self.shUnits.addItem(*u.mm)
        self.shUnits.addItem(*u.inch)
        self.shUnits.addItem(*u.cm)
        self.shUnits.addItem(*u.ln)

        self.twistUnits.addItem(*u.inch)
        self.twistUnits.addItem(*u.cm)
        self.twistUnits.addItem(*u.mm)
        self.twistUnits.addItem(*u.ln)

        self.vUnits.addItem(*u.mps)
        self.vUnits.addItem(*u.kmh)
        self.vUnits.addItem(*u.fps)
        self.vUnits.addItem(*u.mph)
        self.vUnits.addItem(*u.kt)

        self.distUnits.addItem(*u.m)
        self.distUnits.addItem(*u.ft)
        self.distUnits.addItem(*u.yd)
        self.distUnits.addItem(*u.km)
        self.distUnits.addItem(*u.mi)
        self.distUnits.addItem(*u.nm)

        self.tempUnits.addItem(*u.c)
        self.tempUnits.addItem(*u.f)
        self.tempUnits.addItem(*u.k)
        self.tempUnits.addItem(*u.r)

        self.wUnits.addItem(*u.gr)
        self.wUnits.addItem(*u.g)
        self.wUnits.addItem(*u.kg)
        self.wUnits.addItem(*u.lb)
        # self.wUnits.addItem(*u.n)
        # self.wUnits.addItem(*u.oz)

        self.lnUnits.addItem(*u.inch)
        self.lnUnits.addItem(*u.cm)
        self.lnUnits.addItem(*u.mm)
        self.lnUnits.addItem(*u.ln)

        self.dUnits.addItem(*u.inch)
        self.dUnits.addItem(*u.cm)
        self.dUnits.addItem(*u.mm)
        self.dUnits.addItem(*u.ln)

        self.pUnits.addItem(*u.mmhg)
        self.pUnits.addItem(*u.inhg)
        self.pUnits.addItem(*u.bar)
        self.pUnits.addItem(*u.hpa)
        self.pUnits.addItem(*u.psi)

        self.dropUnits.addItem(*u.cm)
        self.dropUnits.addItem(*u.inch)
        self.dropUnits.addItem(*u.mm)
        self.dropUnits.addItem(*u.ln)
        self.dropUnits.addItem(*u.m)
        self.dropUnits.addItem(*u.yd)
        self.dropUnits.addItem(*u.ft)

        self.angleUnits.addItem(*u.deg)
        self.angleUnits.addItem(*u.rad)
        self.angleUnits.addItem(*u.mrad)
        self.angleUnits.addItem(*u.ths)

        self.pathUnits.addItem(*u.mil)
        self.pathUnits.addItem(*u.moa)
        self.pathUnits.addItem(*u.mrad)
        self.pathUnits.addItem(*u.ths)
        self.pathUnits.addItem(*u.cm100m)
        self.pathUnits.addItem(*u.in100yd)

        self.eUnits.addItem(*u.ftlb)
        self.eUnits.addItem(*u.j)

    def load_general_settings(self):
        """loads last general settings from settings.ini"""

        if 'Locale' in self.config:
            locale = self.config['Locale']['current']
            self.Language.setCurrentIndex(self.languages.index(locale))
        else:
            self.save_language_settings()

        if 'General' in self.config:
            exp_dfed = self.config.getboolean('General', 'exp_dfed')
            self.xdfed.setChecked(exp_dfed)
        else:
            self.save_exp_dfed()

    def load_unit_settings(self):
        """loads last unit settings from settings.ini"""

        widgets = self.tabUnits.findChildren(QComboBox)
        if 'Units' in self.config:
            for i in self.config['Units']:
                for w in widgets:
                    if i == w.objectName().lower():
                        w.setCurrentIndex(w.findData(self.config['Units'][i]))
        else:
            self.save_units_settings()

    def save_exp_dfed(self):
        """
        saves to settings.ini if it's enabled experimental
        drag function editor ballistics calculation API here
        """

        exp_dfed = self.xdfed.isChecked()
        if not 'General' in self.config:
            self.config.add_section('General')
        self.config.set('General', 'exp_dfed', str(exp_dfed))

    def save_language_settings(self):
        """saves language settings to settings.ini"""

        locale = self.Language.currentData()
        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)

        if 'Locale' not in self.config:
            self.config.add_section('Locale')

        self.config.set('Locale', 'system', QLocale.system().name().split('_')[1].lower())
        if locale != 'en':
            if os.path.isfile(f'translate/eng-{locale}.qm'):
                self.config.set('Locale', 'current', locale)
            else:
                locale = self.config['Locale']['system']
                self.config.set('Locale', 'current', locale)
        else:
            self.config.set('Locale', 'current', locale)

    def save_units_settings(self):
        """saves _cur_units settings to settings.ini"""

        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)
        if 'Units' not in self.config:
            self.config.add_section('Units')
        for w in self.tabUnits.findChildren(QComboBox):
            self.config.set('Units', w.objectName(), str(w.currentData()))

    def save_extensions_settings(self):
        """saves which extensions are enabled to settings.ini"""

        # config = configparser.ConfigParser()
        # config.read(CONFIG_PATH)
        children = self.tabExtensions.findChildren(QCheckBox)
        for ch in children:
            self.config.set('Extensions', ch.objectName(), str(ch.isChecked()))

    # def accept(self) -> None:
    #     self.save_language_settings()
    #     self.save_exp_dfed()
    #     self.save_units_settings()
    #     self.save_extensions_settings()
    #     self.save_cfg()
    #     super().accept()

    def retranslateUi(self, AppSettings):
        super().retranslateUi(AppSettings)
        _translate = QCoreApplication.translate
        self.inch = (_translate('AppSettings', ' inch'), DistanceInch)
        self.ln = (_translate('AppSettings', ' ln'), DistanceLine)
        self.yd = (_translate('AppSettings', ' yd'), DistanceYard)
        self.ft = (_translate('AppSettings', ' ft'), DistanceFoot)
        self.mm = (_translate('AppSettings', ' mm'), DistanceMillimeter)
        self.cm = (_translate('AppSettings', ' cm'), DistanceCentimeter)
        self.m = (_translate('AppSettings', ' m'), DistanceMeter)
        self.km = (_translate('AppSettings', ' km'), DistanceKilometer)
        self.mi = (_translate('AppSettings', ' mi'), DistanceMile)
        self.nm = (_translate('AppSettings', ' nm'), DistanceNauticalMile)
        self.rad = (_translate('AppSettings', ' rad'), AngularRadian)
        self.deg = (_translate('AppSettings', ' °'), AngularDegree)
        self.mrad = (_translate('AppSettings', ' mrad'), AngularMRad)
        self.ths = (_translate('AppSettings', ' ths'), AngularThousand)
        self.mil = (_translate('AppSettings', ' mil'), AngularMil)
        self.moa = (_translate('AppSettings', ' moa'), AngularMOA)
        self.cm100m = (_translate('AppSettings', ' cm/100m'), AngularCmPer100M)
        self.in100yd = (_translate('AppSettings', ' in/100yd'), AngularInchesPer100Yd)
        self.ftlb = (_translate('AppSettings', ' ft*lb'), EnergyFootPound)
        self.j = (_translate('AppSettings', ' J'), EnergyJoule)
        self.mmhg = (_translate('AppSettings', ' mmHg'), PressureMmHg)
        self.inhg = (_translate('AppSettings', ' inHg'), PressureInHg)
        self.bar = (_translate('AppSettings', ' bar'), PressureBar)
        self.hpa = (_translate('AppSettings', ' hPa'), PressureHP)
        self.psi = (_translate('AppSettings', ' psi'), PressurePSI)
        self.gr = (_translate('AppSettings', ' gr'), WeightGrain)
        self.g = (_translate('AppSettings', ' g'), WeightGram)
        self.kg = (_translate('AppSettings', ' kg'), WeightKilogram)
        self.lb = (_translate('AppSettings', ' lb'), WeightPound)
        self.n = (_translate('AppSettings', ' N'), WeightNewton)
        self.oz = (_translate('AppSettings', ' oz'), WeightOunce)
        self.c = (_translate('AppSettings', ' °C'), TemperatureCelsius)
        self.f = (_translate('AppSettings', ' °F'), TemperatureFahrenheit)
        self.k = (_translate('AppSettings', ' °K'), TemperatureKelvin)
        self.r = (_translate('AppSettings', ' °R'), TemperatureRankin)
        self.mps = (_translate('AppSettings', ' m/s'), VelocityMPS)
        self.kmh = (_translate('AppSettings', ' km/h'), VelocityKMH)
        self.fps = (_translate('AppSettings', ' ft/s'), VelocityFPS)
        self.mph = (_translate('AppSettings', ' mph'), VelocityMPH)
        self.kt = (_translate('AppSettings', ' kt'), VelocityKT)
