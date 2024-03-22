# CALL, TEXT, AND EMAIL AUTOMATE

# It's been a while since we last spoke about purchasing a Mercedes-Benz. Let's pick up where we left off.
# Are you still on the lookout for a Mercedes-Benz?
# Let me know with a simple Y or N.

# Got it, thanks for the update!
# If you find yourself considering a Mercedes-Benz in the future, feel free to reach out.

# Panta Mohan 10:25 AM

import pyautogui
import time

# FAIL SAFE
pyautogui.FAILSAFE = True

time.sleep(3)
# Range will be the number of clients dialed
for i in range(1):
    # Call
    pyautogui.moveTo(890, 451, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # Select
    pyautogui.moveTo(1044, 615, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # Left Voicemail
    pyautogui.moveTo(1000, 679, .1)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(.1)
    # Log Call
    pyautogui.moveTo(1446, 612, .2)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(.1)
    # Text
    pyautogui.moveTo(1116, 459, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # Text Template
    pyautogui.moveTo(1144, 584, .2)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(1)
    # Select Txt Temp
    pyautogui.moveTo(962, 581, .2)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(.5)
    # Click Add
    pyautogui.moveTo(1661, 898, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.5)
    # OPT IN
    pyautogui.moveTo(1455, 583, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # RESEND
    pyautogui.moveTo(1431, 639, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
    # EMAIL
    pyautogui.moveTo(1004, 453, .2)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(.2)
    # Scroll Down
    pyautogui.scroll(-50)
    time.sleep(.5)
    # Move to text area
    pyautogui.moveTo(772, 749, .2)
    time.sleep(.2)
    pyautogui.leftClick()
    time.sleep(.5)
    # Type write 'a'
    pyautogui.write('a')
    time.sleep(.5)
    # New Template Folder with GENIUS
    pyautogui.moveTo(1358, 1053, .1)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.5)
    # Select Template
    pyautogui.moveTo(887, 556, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(1)
    # Click add
    pyautogui.moveTo(1661, 905, .2)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    # # Click Foreground
    # pyautogui.moveTo(1352, 293, .2)
    # time.sleep(.1)
    # pyautogui.leftClick()
    # time.sleep(.1)
    # # # # Scroll Down
    # pyautogui.scroll(-50)
    # time.sleep(.5)
    # Send Email
    pyautogui.moveTo(1463, 1063, .2)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(.1)
    # Next Client
    pyautogui.moveTo(1783, 592, .2)
    time.sleep(.1)
    pyautogui.leftClick()
    time.sleep(.1)
