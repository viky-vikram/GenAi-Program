import pyautogui
import time

# Small pause between PyAutoGUI calls and enable failsafe (move mouse to top-left to abort)
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

print("Starting in 3 seconds... move mouse to top-left to abort if needed.")
time.sleep(3)

# Move to (100, 100) and perform a left click
pyautogui.moveTo(100, 100, duration=1)
time.sleep(0.5)
pyautogui.click(100, 100, button='left')

# Move to (200, 100) and perform a right click
pyautogui.moveTo(200, 100, duration=1)
time.sleep(0.5)
pyautogui.click(200, 100, button='right')

# Move to (300, 100) and perform a double click
pyautogui.moveTo(300, 100, duration=1)
time.sleep(0.5)
pyautogui.doubleClick(300, 100)

# Scroll up then down at the current mouse position (positive = up, negative = down)
time.sleep(0.5)
pyautogui.scroll(500)   # scroll up
time.sleep(0.5)
pyautogui.scroll(-500)  # scroll down

print("Actions complete.")
