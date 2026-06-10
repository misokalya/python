
import csv
from datetime import datetime
from product import Product
from sale import Sale

class Store:
    def __init__(self):
        self.products = []
        self.sales = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        for product in self.products:
            print(product)

    def make_sale(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                if quantity > product.quantity:
                    print("Insufficient stock.")
                    return

                product.quantity -= quantity

                sale = Sale(
                    len(self.sales) + 1,
                    product.name,
                    quantity,
                    quantity * product.price
                )

                self.sales.append(sale)
                print("Sale recorded successfully.")
                return

        print("Product not found.")

    def view_sales(self):
        for sale in self.sales:
            print(sale)

    def total_revenue(self):
        return sum(s.total_amount for s in self.sales)

    def analytics(self):
        summary = {}

        for sale in self.sales:
            summary[sale.product_name] = summary.get(
                sale.product_name, 0
            ) + sale.quantity_sold

        if not summary:
            print("No sales available.")
            return

        most = max(summary, key=summary.get)
        least = min(summary, key=summary.get)

        print(f"Most Sold Product: {most} ({summary[most]} units)")
        print(f"Least Sold Product: {least} ({summary[least]} units)")
        print(f"Total Revenue: Tsh {self.total_revenue():,.0f}")

    def save_products(self):
        with open("products.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Product ID","Name","Price","Quantity"])

            for product in self.products:
                writer.writerow(product.to_list())

    def load_products(self):
        try:
            with open("products.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)

                self.products.clear()

                for row in reader:
                    self.products.append(Product(*row))

        except FileNotFoundError:
            pass

    def save_sales(self):
        with open("sales.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Sale ID","Product","Quantity","Amount","DateTime"]
            )

            for sale in self.sales:
                writer.writerow(sale.to_list())

    def load_sales(self):
        try:
            with open("sales.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)

                self.sales.clear()

                for row in reader:
                    self.sales.append(
                        Sale(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            datetime.fromisoformat(row[4])
                        )
                    )
        except FileNotFoundError:
            pass
