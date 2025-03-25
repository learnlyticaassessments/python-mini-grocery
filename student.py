class GroceryManager:
    def add_product(self, products, name, price, quantity=1, category=None):
        # TODO: Implement this method
        pass

    def total_inventory_value(self, products, price_modifier=lambda p: p["price"]):
        # TODO: Implement this method
        pass

def main():
    # Create an instance of GroceryManager
    gm = GroceryManager()

    # Example usage: Adding products
    products = []
    gm.add_product(products, "Apples", 3.0, 5, category="Fruits")
    gm.add_product(products, "Bread", 2.0, category="Bakery")
    gm.add_product(products, "Milk", 2.0, 3, category="Dairy")
    gm.add_product(products, "Eggs", 0.5, 12, category="Dairy")

    # Display the products
    print("Products:", products)

    # Calculate and display the total inventory value
    print("Total inventory value:", gm.total_inventory_value(products))

    # Calculate and display the total inventory value with a discount
    print("Total inventory value with discount:", gm.total_inventory_value(products, lambda p: p["price"] * 0.9))


if __name__ == "__main__":
    main()
