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
    try:
        with open('config.toml', 'rb') as fp:
            config = tomllib.load(fp)
        base_cfg = config['base_cfg']
        icon = base_cfg['icon']
        with open(base_cfg['theme'], 'r') as fp:
            qss = fp.read()
    except IOError:
        icon = None
        qss = None

    App = QApplication(sys.argv)

    # NATIVE DARK THEME
    DarkTheme().setup(App)

    App.setWindowIcon(QIcon(icon))
    App.setStyleSheet(qss)

    window = MainWindow(App)
    window.show()

    App.exec_()


if __name__ == '__main__':
    main()
