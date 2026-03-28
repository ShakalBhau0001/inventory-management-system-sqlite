from datetime import datetime
from core.database.manager import (
    DatabaseManager,
    Item,
    GET_ALL_ITEMS,
    INSERT_ITEM,
    UPDATE_ITEM,
    DELETE_ITEM,
    COUNT_ITEMS,
    COUNT_LOW_STOCK,
    GET_TOP_ITEMS_BY_QTY,
    GET_EXPORT_DATA,
)


class ItemService:
    def __init__(self, db: DatabaseManager):
        self.db = db

    def get_all(self) -> list[Item]:
        return [self._to_item(r) for r in self.db.fetchall(GET_ALL_ITEMS)]

    def add(self, name, category_id, quantity, price, min_stock, supplier) -> bool:
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if category_id == 0:
            raise ValueError("Please select a category.")
        return self.db.execute(
            INSERT_ITEM,
            (
                name.strip(),
                category_id,
                quantity,
                price,
                min_stock,
                supplier,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )

    def update(
        self, item_id, name, category_id, quantity, price, min_stock, supplier
    ) -> bool:
        return self.db.execute(
            UPDATE_ITEM,
            (name, category_id, quantity, price, min_stock, supplier, item_id),
        )

    def delete(self, item_id: int) -> bool:
        return self.db.execute(DELETE_ITEM, (item_id,))

    def count(self) -> int:
        return self.db.scalar(COUNT_ITEMS) or 0

    def count_low_stock(self) -> int:
        return self.db.scalar(COUNT_LOW_STOCK) or 0

    def top_by_quantity(self, limit: int = 10) -> list[tuple]:
        return [
            (r["name"], r["quantity"])
            for r in self.db.fetchall(GET_TOP_ITEMS_BY_QTY, (limit,))
        ]

    def get_export_data(self) -> list[tuple]:
        return [tuple(r) for r in self.db.fetchall(GET_EXPORT_DATA)]

    @staticmethod
    def _to_item(row) -> Item:
        return Item(
            id=row["id"],
            name=row["name"],
            category_id=0,
            quantity=row["quantity"],
            price=row["price"],
            min_stock=row["min_stock"],
            supplier=row["supplier"] or "",
            date_added=row["date_added"] or "",
            category_name=row[2] or "",
        )
