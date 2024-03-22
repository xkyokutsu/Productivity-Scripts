# UNSUBSCRIBE LOOP

import pyautogui
import time

# failsafe
pyautogui.FAILSAFE = True

time.sleep(3)
# Range will be the number of clients dialed
for i in range(1):
    # #1 Green Info Box
    pyautogui.moveTo(691, 266, .2)
    # Pause for (x)
    time.sleep(.1)
    # Left Click mouse
    pyautogui.leftClick()
    # Pause for (x)
    time.sleep(.5)
    # #2 Down Arrow Tab
    pyautogui.moveTo(1044, 255, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # #3 Unsubscribe Email
    pyautogui.moveTo(861, 295, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # # Confirm
    pyautogui.moveTo(1404, 732, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # #2 Down Arrow Tab
    pyautogui.moveTo(1044, 255, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # #4 Unsubscribe Text
    pyautogui.moveTo(855, 408, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # # Confirm
    pyautogui.moveTo(1404, 732, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # #2 Down Arrow Tab
    pyautogui.moveTo(1044, 255, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # #5 Unsubscribe Phone
    pyautogui.moveTo(856, 476, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # # Confirm
    pyautogui.moveTo(1404, 732, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.3)
    # Next Client
    pyautogui.moveTo(1783, 592, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
