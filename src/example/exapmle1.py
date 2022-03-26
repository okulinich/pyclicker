# https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions

import pyautogui
button7location = pyautogui.locateOnScreen('img/example/calcB7Inactive.png')
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
