import yfinance as yf


ticker = input("Enter the ticker: ")
from_data = input("Enter the start date (YYYY-MM-DD): ")
to_date = input("Enter the end date (YYYY-MM-DD): ")


stock_data = yf.download(ticker, start=from_data, end=to_date)
stock_data.to_html("CurrencyCalc.html")
print("Stock data written to CurrencyCalc.html")