from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class StatCard(QGroupBox):
    def __init__(self, title, value, color, parent=None):
        super().__init__(parent)
        self.setFixedHeight(100)
        self.setStyleSheet(
            f"QGroupBox {{ border: 3px solid {color}; border-radius: 10px; }}"
        )
        layout = QVBoxLayout()
        t = QLabel(title)
        t.setAlignment(Qt.AlignCenter)
        t.setStyleSheet("font-size: 14px; color: #666;")
        self._val = QLabel(value)
        self._val.setAlignment(Qt.AlignCenter)
        self._val.setStyleSheet(f"font-size: 32px; font-weight: bold; color: {color};")
        layout.addWidget(t)
        layout.addWidget(self._val)
        self.setLayout(layout)

    def set_value(self, value: str):
        self._val.setText(value)
