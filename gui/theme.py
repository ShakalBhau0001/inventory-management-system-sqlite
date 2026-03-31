APP_STYLE = """
    QWidget { background-color: #f5f5f5; font-family: 'Segoe UI'; }
    QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
        padding: 8px; border: 2px solid #ddd; border-radius: 5px;
        background-color: white; font-size: 14px; }
    QLineEdit:focus, QComboBox:focus { border-color: #4CAF50; }
    QPushButton {
        padding: 10px 20px; background-color: #4CAF50; color: white;
        border: none; border-radius: 5px; font-size: 14px; font-weight: bold; }
    QPushButton:hover { background-color: #45a049; }
    QPushButton:pressed { background-color: #3d8b40; }
    QTableWidget { gridline-color: #ddd; background-color: white;
        alternate-background-color: #f9f9f9; }
    QTableWidget::item { padding: 8px; }
    QTableWidget::item:selected { background-color: #4CAF50; color: white; }
    QHeaderView::section { background-color: #2196F3; color: white;
        padding: 10px; font-weight: bold; border: none; }
    QTabWidget::pane { border: 1px solid #ddd; background-color: white; }
    QTabBar::tab { background-color: #e0e0e0; padding: 10px 20px; margin-right: 2px; }
    QTabBar::tab:selected { background-color: #4CAF50; color: white; }
    QGroupBox { font-weight: bold; border: 2px solid #ddd; border-radius: 5px;
        margin: 10px; padding-top: 10px; }
"""
COLOR_INFO = "#2196F3"
COLOR_DANGER = "#f44336"
COLOR_SUCCESS = "#4CAF50"
