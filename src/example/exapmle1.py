# https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

import pyautogui
import time

bot_db = ["Dogecoin_click_bot"]

button7location = pyautogui.locateOnScreen('img/telegram/search.png', confidence=0.9)
print(button7location)
#Box(left=1416, top=562, width=50, height=41)
print(button7location[0])
#1416
print(button7location.left)
#1416
button7point = pyautogui.center(button7location)
print(button7point)
#Point(x=1441, y=582)
print(button7point[0])
#1441
print(button7point.x)
#1441
button7x, button7y = button7point
pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found
#pyautogui.click('calc7key.png') # a shortcut version to click on the center of where the 7 button was found
pyautogui.write(bot_db[0])
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
buttonStartLoc = pyautogui.locateOnScreen('img/telegram/start-bot.png', confidence=0.9)
buttonStartPoint = pyautogui.center(buttonStartLoc)
buttonStartLocX, buttonStartLocY = buttonStartPoint
pyautogui.click(buttonStartLocX, buttonStartLocY)
