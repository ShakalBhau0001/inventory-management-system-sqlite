from core.database.manager import (
    DatabaseManager,
    GET_LOW_STOCK_ITEMS,
    GET_FULL_INVENTORY,
    GET_CATEGORY_REPORT,
)


class ReportService:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def low_stock(self) -> str:
        rows = self.db.fetchall(GET_LOW_STOCK_ITEMS)
        lines = ["LOW STOCK REPORT", "=" * 50, ""]
        if rows:
            for r in rows:
                lines += [
                    f"Item: {r['name']}",
                    f"Category: {r[1] or 'N/A'}",
                    f"Current: {r['quantity']}  Min: {r['min_stock']}",
                    "-" * 30,
                ]
        else:
            lines.append("No items are currently low in stock.")
        return "\n".join(lines)

    def full_inventory(self) -> str:
        rows = self.db.fetchall(GET_FULL_INVENTORY)
        lines = ["FULL INVENTORY REPORT", "=" * 50, ""]
        total = 0.0
        for r in rows:
            val = r["quantity"] * r["price"]
            total += val
            lines += [
                f"Item: {r['name']}",
                f"Category: {r[1] or 'N/A'}",
                f"Qty: {r['quantity']}  Price: ${r['price']:.2f}  Value: ${val:.2f}",
                f"Supplier: {r['supplier'] or 'N/A'}",
                "-" * 30,
            ]
        lines.append(f"\nTOTAL VALUE: ${total:.2f}")
        return "\n".join(lines)

    def by_category(self) -> str:
        rows = self.db.fetchall(GET_CATEGORY_REPORT)
        lines = ["CATEGORY REPORT", "=" * 50, ""]
        for r in rows:
            lines += [
                f"Category: {r[0]}",
                f"Items: {r[1] or 0}  Value: ${r[2] or 0:.2f}",
                "-" * 30,
            ]
        return "\n".join(lines)
