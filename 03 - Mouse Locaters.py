import pyautogui
import time

# Gives the python file some time before continuing
for i in range(6):
    # Print location of mouse
    time.sleep(3)
    print(pyautogui.position())
