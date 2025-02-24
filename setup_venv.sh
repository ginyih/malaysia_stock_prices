#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python first."
    exit 1
fi

# Create a virtual environment named 'venv'
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Notify user that the setup is complete
echo "Setup complete. The virtual environment is now activated."
echo "To deactivate, use the command: deactivate"
