import yfinance as yf
import pandas as pd

portfolio = {}

def add_stock(ticker, quantity, buy_price):
    """Add a stock to the portfolio."""
    if ticker in portfolio:
        print(f"Stock {ticker} is already in the portfolio.")
        return
    
    portfolio[ticker] = {"Quantity": quantity, "Buy Price": buy_price}
    print(f"Added {ticker} to your portfolio.")

def remove_stock(ticker):
    """Remove a stock from the portfolio."""
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from your portfolio.")
    else:
        print(f"Stock {ticker} is not in your portfolio.")

def fetch_real_time_price(ticker):
    """Fetch the real-time price of a stock."""
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")["Close"][-1]
        return round(current_price, 2)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def view_portfolio():
    """View the portfolio with real-time prices and performance."""
    if not portfolio:
        print("Your portfolio is empty.")
        return
    
    portfolio_data = []
    for ticker, data in portfolio.items():
        current_price = fetch_real_time_price(ticker)
        if current_price is not None:
            profit_loss = (current_price - data["Buy Price"]) * data["Quantity"]
            portfolio_data.append({
                "Ticker": ticker,
                "Quantity": data["Quantity"],
                "Buy Price": data["Buy Price"],
                "Current Price": current_price,
                "Profit/Loss": round(profit_loss, 2)
            })
    
    # Display portfolio in a table
    df = pd.DataFrame(portfolio_data)
    print("\nYour Portfolio:\n")
    print(df.to_string(index=False))

def main():
    """Main function to interact with the user."""
    print("Welcome to the Stock Portfolio Tracker!")
    
    while True:
        print("\nMenu:")
        print("1. Add a stock")
        print("2. Remove a stock")
        print("3. View portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            ticker = input("Enter stock ticker: ").strip().upper()
            quantity = int(input("Enter quantity: ").strip())
            buy_price = float(input("Enter buy price: ").strip())
            add_stock(ticker, quantity, buy_price)
        
        elif choice == "2":
            ticker = input("Enter stock ticker to remove: ").strip().upper()
            remove_stock(ticker)
        
        elif choice == "3":
            view_portfolio()
        
        elif choice == "4":
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
