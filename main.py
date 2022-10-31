import sys
import tomllib

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from gui import MainWindow, DarkTheme


def load_qss(file_name):
    """use setStylesheet(load_qss(filename))"""
    try:
        with open(file_name, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        return ''


def main():
    with open('config.toml', 'rb') as fp:
        cfg = tomllib.load(fp)
    base_cfg = cfg['base_cfg']
    try:
        with open(base_cfg['theme'], 'r') as fp:
            qss = fp.read()
    except IOError:
        qss = ""

    # os.chdir(os.path.dirname(__file__))
    App = QApplication(sys.argv)

    # _id = QtGui.QFontDatabase.addApplicationFont("Bank Gothic Light BT.ttf")
    # fid = QtGui.QFontDatabase.applicationFontFamilies(_id)
    # font = QtGui.QFont("BankGothic Lt BT")
    # font = QtGui.QFont("Segoe UI Historic")
    # app.setFont(font)

    # NATIVE DARK THEME
    from gui.dark_theme import DarkTheme
    DarkTheme().setup(App)

    print(base_cfg['theme'])
    App.setWindowIcon(QIcon(base_cfg['icon']))
    App.setStyleSheet(qss)

    window = MainWindow(App)
    window.show()

    App.exec_()


if __name__ == '__main__':
    main()
