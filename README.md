# Malaysia Stock Prices to Google Sheets
Fetches the latest stock prices of Malaysian stocks and stores them in a Google Sheet.

## Prerequisites
1. Make sure you have Python 3 installed:
   - Open Command Prompt by pressing `Windows + R`, typing `cmd`, and hitting Enter.
   - Type `python --version` and press Enter. This will show the installed version of Python (if any).
      - If Python is installed, you should see the version number (e.g., `Python 3.x.x`).
      - If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).
      - 
2. Ensure `pip` is installed:
   - Python 3.4 and later versions come with `pip` installed by default. So, after installing Python, you should already have `pip` available.
   - You can check if `pip --version` is installed by typing in the Command Prompt. This will show installed version of pip.
   - If `pip` is not installed or you want to reinstall it, follow these steps:
      - Download [pip](https://bootstrap.pypa.io/get-pip.py) here.
      - Open Command Prompt where you downloaded `get-pip.py`.
      - Navigate to the folder where `get-pip.py` is located, or use the full path to the script.
      - Run the following command `python get-pip.py`
      - 
3. Ensure `venv` is installed (Note: You will need pip for this as mentioned on step 2 above):
   - If you have Python 3.3 or later, `venv` is already included. If you're using an earlier version, proceed below:
      - Open command prompt and type `pip install virtualenv` to install venv.
      - 
4. Acquire your Google `credentials.json` file. Refer to `How to acquire your Google credentials.json` section below.
   - Place your credentials.json in this project's root path (whereever in your disk location you chose to clone this project on):
   ```bash
      malaysia_stock_price
      ├── credentials.json (here)
      ├── README.md
      ├── package.json
      ├── stock_price_fetcher/
      │   ├── __init__.py
      │   ├── config.json
      │   └── utilsfetch_stock_data.py

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ginyih/malaysia_stock_prices.git
   cd malaysia_stock_prices
2. Setup virtual environment by running the following command:
   ```bash
   ./setup_venv.bat
   or
   ./setup_venv.sh (if you are using Linux/macOs)
3. Activate virtual environment by running the following command:
   ```bash
   ./venv/Scripts/activate.bat (if standard Window Command Prompt)
   or
   ./venv/Scripts/activate.ps1 (if using Window PowerShell)
   or
   source venv/bin/activate (if using Linux)
4. Finally to run the script by running the following command:
   ```bash
   python fetch.py

## How to acquire your Google `credentials.json`
1. **Go to Google Cloud Console**:
   - Visit the [Google Cloud Console](https://console.developers.google.com/).
   - Click on **ENABLE APIS AND SERVICES** button
2. **Enable the Google Sheets API**:
   - Navigate to **APIs & Services** → **Library**.
   - Search for **Google Sheets API** and enable it.
   - Also, enable the **Google Drive API** if required for accessing the sheet.
3. **Create a Service Account**:
   - In the Google Cloud Console, go to **APIs & Services** → **Credentials**.
   - Click on **Create Credentials** and choose **Service Account**.
   - Set up the service account (provide a name, and select the **Editor** role, or a more restrictive role like **Viewer**).
   - Once the service account is created, click on it to manage the account.
   - Under the **Keys** section, click **Add Key** → **Create new key** and choose **JSON** as the key type.
   - The JSON file will automatically download to your computer. Place the JSON file directly in the root project.
5. **Share Your Google Sheet with the Service Account**:
   - Open your Google Sheet.
   - Click the **Share** button in the top-right corner.
   - Enter the service account’s email (from the `client_email` field of the `credentials.json` file).
   - Set the permissions to **Editor** or **Viewer**, depending on your needs.
