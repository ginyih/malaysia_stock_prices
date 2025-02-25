# Malaysia Stock Prices to Google Sheets
Fetches the latest stock prices of Malaysian stocks and stores them in a Google Sheet.

## Prerequisites
1. Make sure you have `git` installed:
   - You can download and install it from the [git](https://git-scm.com/downloads/win).

2. Make sure you have Python 3 installed:
   - Open Command Prompt by pressing `Windows + R`, typing `cmd`, and hitting Enter.
   - Type `python --version` and press Enter. This will show the installed version of Python (if any).
      - If Python is installed, you should see the version number (e.g., `Python x.x.x`).
      - If Python is not installed, you can download and install it from the [Python](https://www.python.org/downloads/).

3. Ensure `pip` is installed:
   - Python 3.4 and later versions come with `pip` installed by default. So, after installing Python, you should already have `pip` available.
   - You can check if `pip --version` is installed by typing in the Command Prompt. This will show installed version of pip.
   - If `pip` is not installed or you want to reinstall it, follow these steps:
      - Download [pip](https://bootstrap.pypa.io/get-pip.py) here.
      - Open Command Prompt where you downloaded `get-pip.py`.
      - Navigate to the folder where `get-pip.py` is located, or use the full path to the script.
      - Run the following command `python get-pip.py`

4. Ensure `venv` is installed (Note: You will need pip for this as mentioned on step 2 above):
   - If you have Python 3.3 or later, `venv` is already included. If you're using an earlier version, proceed below:
      - Open command prompt and type `pip install virtualenv` to install venv.

5. Enable Google APIs (Google Drive and Google Sheet), create a Service Account, and acquire credentials JSON file. Please refer to the bottom section on how to.
   - Rename the credentials JSON file you downloaded from Google to `credentials.json`. 

6. Share Your Google Sheet with the Service Account you created:
   - Open your Google Sheet.
   - Click the **Share** button in the top-right corner.
   - Enter the service account's email (from the `client_email` field of the `credentials.json` file) or just copy from your [Google Cloud Console](https://console.developers.google.com/).
   - Set the permissions to **Editor** and Send.

## Setup
1. Clone the repository by typing this in Command Prompt:
   ```
   git clone https://github.com/ginyih/malaysia_stock_prices.git
   ```

2. Change to the project directory (the one you just cloned from step 1 above) by typing this in Command Prompt:
   ```
   cd malaysia_stock_prices
   ```

3. Place your `credentials.json` file you downloaded from step 4 of `Prerequisites` above within the project directory you just cloned:
   ```
      malaysia_stock_price
      ├── credentials.json (here)
      ├── README.md
      ├── config.json
      ├── requirements.txt
      ├── setup_venv.bat
      └── setup_venv.sh
   ```

4. Setup virtual environment (venv) by typing this in Command Prompt:
   - Windows:
      - Command Prompt / Power Shell:
      ```
      ./setup_venv.bat
      ```
   - Linux:
      ```
      ./setup_venv.sh
      ```

5. Activate virtual environment (venv) by typing this in Command Prompt (only choose one depending on your OS, and if Windows then either Command Prompt or Power Shell depending on your terminal of choice):
   - Windows:
      - Command Prompt:
      ```
      ./venv/Scripts/activate.bat
      ```
      - Power Shell:
      ```
      ./venv/Scripts/activate.ps1
      ```
   - Linux:
      ```
      source venv/bin/activate
      ```

6. Finally to run the script by running the following command:
   ```bash
   python fetch.py
   ```

## Note
After setting everything up, on every consecutive script run you just have to start from:
   - Activate venv from step 5 above.
   - Execute fetch.py from step 6 above.
   ```
   ./venv/Scripts/activate.bat
   python fetch.py
   ```

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
   - The JSON file will automatically download to your computer. Rename the JSON file to `credentials.json` and place it directly in the root project.
