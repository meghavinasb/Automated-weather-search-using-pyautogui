# Automated-weather-search-using-pyautogui

## Description
This Python script automates the process of searching for weather information using PyAutoGUI. It prompts the user for the location and temperature unit, opens the Windows search bar, launches the weather application, and retrieves weather details based on user input.

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.6)
- PyAutoGUI (`pip install pyautogui`)

## How It Works
1. The script prompts the user for the city/town/village name and the state.
2. The user is asked to choose the temperature unit (Celsius or Fahrenheit).
3. It opens the Windows search bar and types 'weather' to launch the weather application.
4. It searches for the entered location.
5. It adjusts the temperature unit based on user selection.

## Installation
1. Install Python if not already installed: [Download Python](https://www.python.org/downloads/)
2. Install PyAutoGUI:
   ```sh
   pip install pyautogui
   ```
3. Run the script:
   ```sh
   python script.py
   ```

## Notes
- The script relies on specific screen coordinates for clicking buttons. If the layout of the weather app changes or screen resolution differs, you may need to adjust the coordinates.
- Ensure that Chrome and the Windows weather application are installed on your system.

## Disclaimer
Use this script responsibly. Automating UI interactions can interfere with normal computer usage. Adjust sleep times and coordinates as necessary based on your system configuration.

