@echo off

:: Check if Python is installed
python --version || (
    echo Python is not installed. Please install Python first.
    exit /b 1
)

:: Create a virtual environment named 'venv'
echo Creating virtual environment...
python -m venv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

:: Notify user that the setup is complete
echo Setup complete. The virtual environment is now activated.
echo To deactivate, use the command: deactivate
pause
