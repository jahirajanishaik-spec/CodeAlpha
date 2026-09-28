def stock_portfolio_tracker():
    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }

    print("Available Stocks and Prices per share:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

    portfolio = {}
    print("\nEnter your stock portfolio details (type 'done' when finished):")
    
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not found in price list. Choose from: ", list(stock_prices.keys()))
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        except ValueError:
            print("Please enter a valid integer for quantity.")

    # Calculate total investment value
    print("\n--- Portfolio Summary ---")
    total_investment = 0
    summary_lines = ["Stock Portfolio Summary\n", "Stock\tQuantity\tPrice\tTotal Value\n"]
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        line = f"{stock}\t{qty}\t\t${price}\t${value}"
        print(line)
        summary_lines.append(line + "\n")

    total_line = f"\nTotal Investment Value: ${total_investment}"
    print(total_line)
    summary_lines.append(total_line)

    # Option to save to a file
    save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = "portfolio_summary.txt"
        with open(filename, "w") as file:
            file.writelines(summary_lines)
        print(f"Portfolio successfully saved to {filename}!")

if __name__ == "__main__":
    stock_portfolio_tracker()