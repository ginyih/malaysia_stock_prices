import yfinance as yf
import gspread
import json
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
    tickers = list(stock_datas.values())
    
    # Fetch stock data for all tickers at once using yfinance
    try:
        data = yf.download(tickers, period="1d")['Close']  # Fetch closing prices for the last day

        # Loop through each stock and store its closing price in the stock_data dictionary
        for symbol, ticker in stock_datas.items():
            if ticker in data.columns:  # Check if data for this ticker exists in the dataframe
                stock_prices[symbol] = float(data[ticker].iloc[-1])  # Get the most recent closing price
            else:
                stock_prices[symbol] = None  # If no data found, store None

    except Exception as e:
        print(f"Error occurred: {e}")
    
    return stock_prices


def get_stock_symbols(sheet, stock_name_column_index, stock_tickers):
    # Get the stock symbols starting from the second row in the first column (column A)
    stock_symbols = sheet.col_values(stock_name_column_index)[1:]  # Skip the header (row 1)
    stock_datas = {}
    for symbol in stock_symbols:
        stock_datas.setdefault(symbol, stock_tickers.get(symbol))
    return stock_datas


def update_google_sheet(sheet, stock_price_column_index, stock_prices):
    # Prepare a list to store cell objects to update
    cells_to_update = []
    
    # Loop through the stock prices to prepare cell objects
    for i, (symbol, price) in enumerate(stock_prices.items(), start=2):  # start=2 to skip header row
        if price is not None:
            # Format price with 'RM' prefix, comma delimiter, and 2 decimal places
            formatted_price = f"{price:,.2f}"  # Limit to 2 decimal places
        else:
            # If no price data, show 'No data' instead of None
            formatted_price = "No data"
        
        # Create the cell object and append it to the list (column 10 is the target column for stock prices)
        cell = sheet.cell(i, stock_price_column_index)  # Get the cell object at row i and column 10
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
    
    # Open your sheet (replace with your actual sheet name)
    sheet = client.open(SHEET_NAME).sheet1  # Make sure the sheet is shared with the service account email
    
    # Get stock names from google sheet (column 1)
    stock_tickers = get_stock_symbols(sheet, STOCK_NAME_COLUMN_INDEX, STOCK_TICKERS)

    # Fetch the stock prices
    stock_prices = fetch_stock_prices(stock_tickers)

    # Update Google Sheets
    update_google_sheet(sheet, STOCK_PRICE_COLUMN_INDEX, stock_prices)


if __name__ == "__main__":
    main()
