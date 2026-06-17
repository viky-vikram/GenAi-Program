import pyautogui
import time
from datetime import datetime
import pyperclip
import os

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

today = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_name = f"daily_report_{today}.xlsx"
screenshot_name = f"daily_report_screenshot_{today}.png"

file_path = os.path.join(os.getcwd(), file_name)
screenshot_path = os.path.join(os.getcwd(), screenshot_name)

comment = "Good for outdoor activities"

print("Starting automation in 3 seconds...")
time.sleep(3)

# Open Chrome
print("Step 1. Opening Chrome...")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)

# Open weather website
print("Step 2. Opening weather website...")
url = "https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671"
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyperclip.copy(url)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(8)

# Copy webpage content
print("Step 3. Copying webpage content...")
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

copied_text = pyperclip.paste()

# Extract only useful weather data
lines = copied_text.splitlines()
weather_lines = []

for line in lines:
    line = line.strip()

    if "°" in line or "RealFeel" in line or "Mostly" in line or "Sunny" in line or "Cloudy" in line or "Rain" in line:
        weather_lines.append(line)

weather_data = " | ".join(weather_lines[:5])

if weather_data == "":
    weather_data = "Weather data fetched from AccuWeather"

# Open Excel
print("Step 4. Opening Excel...")
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('excel')
pyautogui.press('enter')
time.sleep(8)

# Open blank workbook
pyautogui.press('enter')
time.sleep(3)

# Paste only 3 columns
print("Step 5. Pasting data into Excel...")
excel_data = (
    "Date & Time\tFetched Weather Data\tComment\n"
    f"{current_time}\t{weather_data}\t{comment}"
)

pyperclip.copy(excel_data)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Save Excel file
pyautogui.hotkey('ctrl', 's')
time.sleep(2)

pyperclip.copy(file_path)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)

# Take screenshot
print("Step 6. Taking screenshot...")
screenshot = pyautogui.screenshot()
screenshot.save(screenshot_path)

print("Completed successfully!")
print("Excel saved as:", file_path)
print("Screenshot saved as:", screenshot_path)