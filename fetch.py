import yfinance as yf
import gspread
import json

from collections import OrderedDict
from oauth2client.service_account import ServiceAccountCredentials


def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config


# Define your Google Sheets API credentials
def authenticate_google_sheets():
    # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]
    scope = [
        "https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/spreadsheets", 
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client


def fetch_stock_prices(stock_datas):
    stock_prices = {}
    
    # Create a list of ticker symbols (the keys from the stock_symbols dictionary)
    tickers = [ticker for data in stock_datas.values() for ticker in data.values() if ticker]

    # Fetch stock data for all tickers at once using yfinance
    try:
        yahoo_data = yf.download(tickers, period="1d")['Close']  # Fetch closing prices for the last day

        # Loop through each stock and store its closing price in the stock_data dictionary
        for data in stock_datas.values():
            (symbol, ticker) = next(iter(data.items()))
            if ticker in yahoo_data.columns:  # Check if data for this ticker exists in the dataframe
                stock_prices[symbol] = float(yahoo_data[ticker].iloc[-1])  # Get the most recent closing price
            else:
                stock_prices[symbol] = None

    except Exception as e:
        print(f"Error occurred: {e}")
    
    return stock_prices


def get_stock_symbols(sheet, column, stock_tickers):
    # Get the stock symbols starting from the second row in the first column (column A)
    stock_symbols = sheet.col_values(column)[1:]  # Skip the header (row 1)
    stock_datas = OrderedDict()
    for row, symbol in enumerate(stock_symbols, start=2):
        ticker = stock_tickers.get(symbol)
        data = {symbol: ticker}
        stock_datas[row] = {symbol: ticker}
    return stock_datas


def update_google_sheet(sheet, column, stock_tickers, stock_prices):
    # Prepare a list to store cell objects to update
    cells_to_update = []

    for row, stock_data in stock_tickers.items():
        symbol = next(iter((stock_data.keys())))
        price = stock_prices.get(symbol)
        if price:
            formatted_price = f"{price:,.2f}"  # Limit to 2 decimal places

            # Create the cell object and append it to the list (column 10 is the target column for stock prices)
            cell = sheet.cell(row, column)
            cell.value = formatted_price
            cells_to_update.append(cell)  # Add the cell to the update list
    
    # Update all cells at once
    sheet.update_cells(cells_to_update)  # Efficient batch update
    
    print("Google Sheet updated successfully!")


def main():
    # Load configuration
    config = load_config()

    # Retrieve the stock tickers and column index
    STOCK_TICKERS = config.get("STOCK_TICKERS")
    SHEET_NAME = config.get("GOOGLE_SHEET_NAME")
    SHEET_TAB_NAME = config.get("SHEET_TAB_NAME")
    STOCK_NAME_COLUMN_INDEX = config.get("STOCK_NAME_COLUMN_INDEX")
    STOCK_PRICE_COLUMN_INDEX = config.get("STOCK_PRICE_COLUMN_INDEX")

    # Authenticate and get the Google Sheets client
    client = authenticate_google_sheets()
    
    # Initialize the correct sheet by tab name
    sheet = None
    all_sheets = client.open(SHEET_NAME)  # Open the spreadsheet by name
    for sheet_tab in all_sheets.worksheets():
        if sheet_tab.title == SHEET_TAB_NAME:
            sheet = sheet_tab
            break

    if sheet:
        # Get stock names from google sheet (column 1)
        stock_tickers = get_stock_symbols(sheet, STOCK_NAME_COLUMN_INDEX, STOCK_TICKERS)

        # Fetch the stock prices
        stock_prices = fetch_stock_prices(stock_tickers)

        # Update Google Sheets
        update_google_sheet(sheet, STOCK_PRICE_COLUMN_INDEX, stock_prices, stock_prices)
    else:
        raise KeyError(f'Tab "{SHEET_TAB_NAME}" does not exist!')


if __name__ == "__main__":
    main()
