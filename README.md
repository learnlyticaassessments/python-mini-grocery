# 🧾 Mini Grocery Tracker

## 🎯 Concepts Tested
✅ Python Lists and Dictionaries  
✅ Function Parameters: Positional, Default, Keyword-only  
✅ Lambda & map usage  
✅ Return value & function as parameter  

## 📌 Problem Statement
Create a lightweight grocery inventory tracker. The system should allow adding product entries with optional category tagging and compute total inventory value using custom price adjustment functions.

## 📌 Operations

### 1. Add Product to List with Flexible Parameters
**Function:**
```python
def add_product(product_list: list, name: str, price: float, quantity: int = 1, *, category="General") -> None
```

### 2. Compute Total Inventory Value with Price Adjuster
**Function:**
```python
def total_inventory_value(product_list: list, price_fn: callable) -> float
```

## ✅ Sample Visible Test Cases

### TC1: Add Full Product
```python
products = []
gm = GroceryManager()
gm.add_product(products, "Apples", 3.0, 5, category="Fruits")
print(products)
# Expected: [{'name': 'Apples', 'price': 3.0, 'quantity': 5, 'category': 'Fruits'}]
```

### TC2: Add with Default Quantity
```python
products = []
gm = GroceryManager()
gm.add_product(products, "Bread", 2.0, category="Bakery")
print(products)
# Expected: [{'name': 'Bread', 'price': 2.0, 'quantity': 1, 'category': 'Bakery'}]
```

### TC3: Total Value with 10% Discount
```python
products = []
gm = GroceryManager()
gm.add_product(products, "Milk", 2.0, 3, category="Dairy")
gm.add_product(products, "Eggs", 0.5, 12, category="Dairy")
total = gm.total_inventory_value(products, lambda p: p["price"] * 0.9)
print(total)
# Expected: 8.46
```
