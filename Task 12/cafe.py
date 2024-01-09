menu = ["Coffee", "Tea", "Milk", "Orange Juice", "Pastry"]
stock_amounts = [15, 12, 6, 20, 6]
stock = dict(zip(menu, stock_amounts))
price_values = [2.99, 3.50, 2, 1.50, 4.99]
price = dict(zip(menu, price_values))
total_stock = 0
for i in menu:
    total_stock += stock[i] * price[i]
print(f"Total stock value £{total_stock}!")