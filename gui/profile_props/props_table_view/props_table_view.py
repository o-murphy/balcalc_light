from PyQt5.QtWidgets import QTableView


class PropsTableView(QTableView):
    def __init__(self, parent=None):
        super(PropsTableView, self).__init__(parent)
        self.setEditTriggers(QTableView.SelectedClicked | QTableView.CurrentChanged)
        self.setSelectionMode(QTableView.SingleSelection)
