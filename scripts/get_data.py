import pandas as pd
import yfinance as yf
import os

# Determine the base directory (project root)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Load the SP500 stock list
# csv_file_path = os.path.join(base_dir, 'sp500_stocks.csv')
# sp500_stocks = pd.read_csv(csv_file_path)

# load etfs
csv_file_path = os.path.join(base_dir, 'etfs.csv')
etf_tickers = pd.read_csv(csv_file_path)

# Directory to save the stock data
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# Function to download stock data
def download_stock_data(symbol, start_date='2021-01-01', end_date='2024-08-27'):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        stock_data.to_csv(os.path.join(data_dir, f'{symbol}.csv'))
        print(f'Successfully downloaded data for {symbol}')
    except Exception as e:
        print(f'Failed to download data for {symbol}: {e}')

# Download data for all SP500 stocks
# for symbol in sp500_stocks['Symbol']:
for symbol in etf_tickers['Symbol']:
    download_stock_data(symbol)
