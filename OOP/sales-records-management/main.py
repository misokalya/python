
from product import Product
from store import Store

store = Store()
store.load_products()
store.load_sales()

while True:
    print("\n=== ELECTRONICS STORE SYSTEM ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Record Sale")
    print("4. View Sales")
    print("5. Analytics")
    print("6. Save Records")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = Product(
            input("Product ID: "),
            input("Product Name: "),
            float(input("Price: ")),
            int(input("Quantity: "))
        )
        store.add_product(product)

    elif choice == "2":
        store.view_products()

    elif choice == "3":
        store.make_sale(
            input("Product ID: "),
            int(input("Quantity Sold: "))
        )

    elif choice == "4":
        store.view_sales()

    elif choice == "5":
        store.analytics()

    elif choice == "6":
        store.save_products()
        store.save_sales()
        print("Records saved successfully.")

    elif choice == "7":
        store.save_products()
        store.save_sales()
        break

    else:
        print("Invalid choice.")
