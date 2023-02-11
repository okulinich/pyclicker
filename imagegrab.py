from PIL import Image, ImageGrab
import cv2
import numpy as np
import os
import time


ERROR = 1
INFO = 2
DEBUG = 3

LOG_LEVEL = DEBUG
# default timeout for the screen operations in seconds
SYSTEM_CMD_TIMEOUT = 1

def LocateImage(image, Region=None, Precision=0.8):
    im2 = ImageGrab.grab(bbox = None)

    img_rgb = np.array(im2)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, LocatedPrecision, min_loc, Position = cv2.minMaxLoc(res)

    if LocatedPrecision > Precision:
        dimensions = template.shape
        return Position[0] + dimensions[1]/2, Position[1] + dimensions[0]/2
    return 0, 0

def PrintLog(log_level, message):
    if log_level >= LOG_LEVEL:
        print(message)

def PrintDebug(str):
    PrintLog(DEBUG, str)

def ExecuteSystemCommand(command):
    exit_status = int()
    os.system(command)
    os.WEXITSTATUS(exit_status)
    PrintDebug(f"command *{command}* exited with status {exit_status}")
    time.sleep(SYSTEM_CMD_TIMEOUT)

def FocusOnWindow(name):
    ExecuteSystemCommand(f"wmctrl -a {name}")

def MouseClick(x, y):
    ExecuteSystemCommand(f"xte 'mousemove {x} {y}'")
    ExecuteSystemCommand("xte 'mousedown 1' && xte 'mouseup 1'")

def TypeText(text):
    ExecuteSystemCommand(f"xte 'str {text}'")




result = LocateImage('/root/Desktop/search.png')
print(result)

FocusOnWindow("Telegram")
MouseClick(int(result[0]), int(result[1]))
TypeText("test")
