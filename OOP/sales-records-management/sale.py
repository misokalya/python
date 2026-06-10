
from datetime import datetime

class Sale:
    def __init__(self, sale_id, product_name, quantity_sold, total_amount, sale_datetime=None):
        self.sale_id = int(sale_id)
        self.product_name = product_name
        self.quantity_sold = int(quantity_sold)
        self.total_amount = float(total_amount)
        self.sale_datetime = sale_datetime or datetime.now()

    def to_list(self):
        return [
            self.sale_id,
            self.product_name,
            self.quantity_sold,
            self.total_amount,
            self.sale_datetime.isoformat()
        ]

    def __str__(self):
        return f"{self.sale_id} | {self.product_name} | Qty:{self.quantity_sold} | Tsh {self.total_amount:,.0f} | {self.sale_datetime}"
