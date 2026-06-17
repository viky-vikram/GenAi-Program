import pyautogui
import time




pyautogui.FAILSAFE = True
time.sleep(3)  # Give user time to prepare

#pyautogui.typewrite("Hello, this is a test message!", interval=0.1)
#time.sleep(0.5)

# Wait and then select all, copy
#time.sleep(1)
#pyautogui.hotkey('ctrl', 'a')  # Select all text
#pyautogui.hotkey('ctrl', 'c')  # Copy the selected text

#pyautogui.keyDown('shift')
#pyautogui.typewrite('aaaabb', interval=0.1)
#pyautogui.keyUp('shift')

screenshot = pyautogui.screenshot()
screenshot.save("test.png")
