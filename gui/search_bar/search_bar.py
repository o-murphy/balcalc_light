from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QLineEdit


class SearchBar(QLineEdit):
    def __init__(self, parent=None):
        super(SearchBar, self).__init__(parent)
        self.retranslateUi(self)

    def retranslateUi(self, SearchBar):
        _translate = QCoreApplication.translate
        SearchBar.setPlaceholderText(_translate("SearchBar", "🔍 Search"))
