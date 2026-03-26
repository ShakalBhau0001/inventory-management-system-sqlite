from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

EXPORT_COLUMNS = [
    "Item Name",
    "Category",
    "Quantity",
    "Price",
    "Min Stock",
    "Supplier",
    "Date Added",
]
X_POS = [50, 140, 240, 290, 345, 410, 490]


def export_pdf(data: list[tuple], filepath: str) -> None:
    c = canvas.Canvas(filepath, pagesize=letter)
    _, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Inventory Report")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 30

    c.setFont("Helvetica-Bold", 9)
    for i, col in enumerate(EXPORT_COLUMNS):
        c.drawString(X_POS[i], y, col)
    y -= 18

    c.setFont("Helvetica", 9)
    for row in data:
        if y < 50:
            c.showPage()
            y = height - 50
        for i, val in enumerate(row):
            c.drawString(X_POS[i], y, str(val or "")[:13])
        y -= 14
    c.save()
