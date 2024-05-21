cost_price = int(input("Enter the cost of the item in rupees: "))
selling_price = int(input("Enter the selling price of the item in rupees: "))

if cost_price > selling_price:
    print("The seller has made the loss of:", cost_price - selling_price, "rupees.")
elif selling_price > cost_price:
    print("The seller has  made the profit of:", selling_price - cost_price, "rupees.")
else:
    print("No profit , no loss is made.")