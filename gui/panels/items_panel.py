from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QLabel,
    QMessageBox,
    QTableWidgetItem,
)
from PyQt5.QtCore import pyqtSignal
from core.services.item_service import ItemService
from core.services.category_service import CategoryService
from gui.components.table_widget import InventoryTable

HEADERS = [
    "ID",
    "Name",
    "Category",
    "Qty",
    "Price",
    "Min Stock",
    "Supplier",
    "Date Added",
]


# Inline validators
def _require_text(widget, field, parent=None) -> bool:
    if not widget.text().strip():
        QMessageBox.warning(parent, "Error", f"{field} required!")
        widget.setFocus()
        return False
    return True


def _require_selection(combo, field, parent=None) -> bool:
    if not combo.currentData():
        QMessageBox.warning(parent, "Error", f"Please select a {field}!")
        return False
    return True


def _confirm_delete(parent, name="this item") -> bool:
    from PyQt5.QtWidgets import QMessageBox

    return (
        QMessageBox.question(
            parent,
            "Confirm Delete",
            f"Delete {name}? This cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
        )
        == QMessageBox.Yes
    )


class ItemsPanel(QWidget):
    data_changed = pyqtSignal()

    def __init__(self, item_svc: ItemService, cat_svc: CategoryService, parent=None):
        super().__init__(parent)
        self.item_svc = item_svc
        self.cat_svc = cat_svc
        self._build_ui()
        self.reload_categories()
        self.reload_items()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        sr = QHBoxLayout()
        self.search_box = QLineEdit(placeholderText="Search items...")
        self.search_box.textChanged.connect(self._filter)
        self.cat_filter = QComboBox()
        self.cat_filter.currentTextChanged.connect(self._filter)
        sr.addWidget(QLabel("Search:"))
        sr.addWidget(self.search_box)
        sr.addWidget(QLabel("Category:"))
        sr.addWidget(self.cat_filter)

        self.table = InventoryTable(HEADERS)
        self.table.itemClicked.connect(self._populate_form)

        fg = QGroupBox("Add / Edit Item")
        fl = QFormLayout()
        self.f_name = QLineEdit()
        self.f_category = QComboBox()
        self.f_quantity = QSpinBox()
        self.f_quantity.setRange(0, 999999)
        self.f_price = QDoubleSpinBox()
        self.f_price.setRange(0, 999999.99)
        self.f_price.setDecimals(2)
        self.f_min_stock = QSpinBox()
        self.f_min_stock.setRange(0, 999999)
        self.f_supplier = QLineEdit()
        fl.addRow("Name:", self.f_name)
        fl.addRow("Category:", self.f_category)
        fl.addRow("Quantity:", self.f_quantity)
        fl.addRow("Price:", self.f_price)
        fl.addRow("Min Stock:", self.f_min_stock)
        fl.addRow("Supplier:", self.f_supplier)

        btns = QHBoxLayout()
        for lbl, slot, style in [
            ("Add", self._add, ""),
            ("Update", self._update, ""),
            ("Delete", self._delete, "QPushButton{background:#f44336;}"),
            ("Clear", self._clear, "QPushButton{background:#9E9E9E;}"),
        ]:
            b = QPushButton(lbl)
            b.clicked.connect(slot)
            if style:
                b.setStyleSheet(style)
            btns.addWidget(b)
        fl.addRow(btns)
        fg.setLayout(fl)

        layout.addLayout(sr)
        layout.addWidget(self.table)
        layout.addWidget(fg)

    def reload_items(self):
        items = self.item_svc.get_all()
        rows = [
            (
                i.id,
                i.name,
                i.category_name,
                i.quantity,
                f"{i.price:.2f}",
                i.min_stock,
                i.supplier,
                i.date_added,
            )
            for i in items
        ]
        self.table.populate(rows, low_stock_col=3, min_stock_col=5)

    def reload_categories(self):
        cats = self.cat_svc.get_all()
        self.f_category.clear()
        self.f_category.addItem("Select Category", 0)
        self.cat_filter.clear()
        self.cat_filter.addItem("All Categories")
        for c in cats:
            self.f_category.addItem(c.name, c.id)
            self.cat_filter.addItem(c.name)

    def _filter(self):
        text = self.search_box.text().lower()
        cat = self.cat_filter.currentText()
        for row in range(self.table.rowCount()):
            show = True
            if text and text not in self.table.item(row, 1).text().lower():
                show = False
            if cat != "All Categories" and self.table.item(row, 2).text() != cat:
                show = False
            self.table.setRowHidden(row, not show)

    def _selected_row(self) -> int:
        item = self.table.currentItem()
        return item.row() if item is not None else -1

    def _populate_form(self, clicked: QTableWidgetItem):
        row = clicked.row()
        self.f_name.setText(self.table.item(row, 1).text())
        idx = self.f_category.findText(self.table.item(row, 2).text())
        if idx >= 0:
            self.f_category.setCurrentIndex(idx)
        self.f_quantity.setValue(int(self.table.item(row, 3).text() or 0))
        self.f_price.setValue(float(self.table.item(row, 4).text() or 0))
        self.f_min_stock.setValue(int(self.table.item(row, 5).text() or 0))
        self.f_supplier.setText(self.table.item(row, 6).text())

    def _clear(self):
        self.f_name.clear()
        self.f_category.setCurrentIndex(0)
        self.f_quantity.setValue(0)
        self.f_price.setValue(0)
        self.f_min_stock.setValue(0)
        self.f_supplier.clear()
        self.table.clearSelection()

    def _add(self):
        if not _require_text(self.f_name, "Item name", self):
            return
        if not _require_selection(self.f_category, "category", self):
            return
        try:
            self.item_svc.add(
                self.f_name.text(),
                self.f_category.currentData(),
                self.f_quantity.value(),
                self.f_price.value(),
                self.f_min_stock.value(),
                self.f_supplier.text(),
            )
            self._clear()
            self.reload_items()
            self.data_changed.emit()
            QMessageBox.information(self, "Success", "Item added!")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def _update(self):
        row = self._selected_row()
        if row < 0:
            QMessageBox.warning(self, "Error", "Select an item to update!")
            return
        self.item_svc.update(
            int(self.table.item(row, 0).text()),
            self.f_name.text(),
            self.f_category.currentData(),
            self.f_quantity.value(),
            self.f_price.value(),
            self.f_min_stock.value(),
            self.f_supplier.text(),
        )
        self._clear()
        self.reload_items()
        self.data_changed.emit()
        QMessageBox.information(self, "Success", "Item updated!")

    def _delete(self):
        row = self._selected_row()
        if row < 0:
            QMessageBox.warning(self, "Error", "Select an item to delete!")
            return
        name = self.table.item(row, 1).text()
        if _confirm_delete(self, f'"{name}"'):
            self.item_svc.delete(int(self.table.item(row, 0).text()))
            self._clear()
            self.reload_items()
            self.data_changed.emit()
            QMessageBox.information(self, "Success", "Item deleted!")
