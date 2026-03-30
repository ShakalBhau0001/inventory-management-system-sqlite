from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QColor


class InventoryTable(QTableWidget):
    def __init__(self, headers: list[str], parent=None):
        super().__init__(parent)
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def populate(self, rows: list, low_stock_col=None, min_stock_col=None):
        self.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.setItem(r, c, QTableWidgetItem(str(val or "")))
            if low_stock_col is not None and min_stock_col is not None:
                try:
                    if int(row[low_stock_col]) <= int(row[min_stock_col]):
                        self.item(r, low_stock_col).setBackground(QColor(255, 200, 200))
                except (ValueError, TypeError):
                    pass
