print("--- Stock Portfolio Tracker ---")

# hardcoded price - dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

print("Available Stocks:", stock_prices)

total_value = 0

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        qty = int(input(f"Enter quantity for {stock}: "))
        price = stock_prices[stock]
        value = price * qty
        total_value = total_value + value
        print(f"{stock}: {qty} x {price} = {value}")
    else:
        print("Stock not found! Try AAPL, TSLA, GOOGL, MSFT")

print("\n---------------------------")
print("Total Investment: $", total_value)
print("---------------------------")

# optional file save
save = input("Save to file? (yes/no): ")
if save == "yes":
    file = open("portfolio.txt", "w")
    file.write(f"Total Investment: ${total_value}\n")
    file.close()
    print("Saved to portfolio.txt")
