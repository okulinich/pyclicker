

import pyautogui
import time
import logging
import os

def find_and_click(image_path):
    button_loc = pyautogui.locateOnScreen(image_path, confidence=0.9)
    if button_loc is None:
        print("Failed to find an image " + image_path)
        return False
    button_point = pyautogui.center(button_loc)
    pyautogui.click(button_point.x, button_point.y)
    return True


bot_db = ["ClickBeeBot"]

if not find_and_click('img/telegram/search.png'):
    exit(1)

pyautogui.write(bot_db[0])
time.sleep(3)
pyautogui.press('enter')

#if not find_and_click('img/telegram/clickbee-join-chats.png'):
#    if not find_and_click('img/telegram/telegram-write-a-message-2.png'):
#        exit(2)
#    pyautogui.write("/start")
#    pyautogui.press('enter')
#    time.sleep(3)

attempts = 0

while True:
    if find_and_click('img/telegram/clickbee-join-chats.png'):
        time.sleep(3)
        if find_and_click('img/telegram/clickbee-join-the-channel.png'):
            time.sleep(3)
            if find_and_click('img/telegram/telegram-join.png'):
                # TODO: mute in case of channel
                pyautogui.press('esc')
                time.sleep(3)
                if find_and_click('img/telegram/clickbee-joined.png'):
                    time.sleep(5)
                    if find_and_click('img/telegram/clickbee-back.png'):
                        time.sleep(5)
                        continue
                    else:
                        # failed to find BACK button
                        exit(1)
                else:
                    # failed to find JOINED button
                    exit(1)
            else:
                # failed to find JOIN button
                exit(1)
        else:
            # failed to find JOIN THE CHANNEL button
            print("No more channels/chats available")
            break
    else:
        # failed to find JOIN CHATS
        if not find_and_click('img/telegram/clickbee-back.png') and not find_and_click('img/telegram/clickbee-back-2.png'):
            if not find_and_click('img/telegram/telegram-write-a-message-2.png') and not find_and_click('img/telegram/telegram-write-a-message-3.png'):
                exit(2)
            pyautogui.write("/start")
            pyautogui.press('enter')
        time.sleep(3)
        #exit(1) exit after several attempts

# while True:
    # if find_and_click('img/telegram/clickbee-message-bots.png'):
        # time.sleep(3)
        # if find_and_click('img/telegram/telegram-staroret.png'):
            # time.sleep(5)
            # pyautogui.press('esc')
            # time.sleep(3)
            # if find_and_click('img/telegram/clickbee-started.png'):
                # time.sleep(5)
                # if find_and_click('img/telegram/clickbee-bot-promotion.png'):
                    # need to save bots name, then forward the last message from bot to current bot

while True:
    if find_and_click('img/telegram/clickbee-more.png'):
        time.sleep(3)
        if find_and_click('img/telegram/clickbee-watch-adds.png'):
            time.sleep(20)
            if not find_and_click('img/telegram/clickbee-watched.png'):
                pyautogui.move(0, -250)
                time.sleep(3)
                pyautogui.vscroll(10)
                time.sleep(3)
                if not find_and_click('img/telegram/clickbee-watched.png'):
                    print("Looks like no more adds are available to watch")
                    break
            time.sleep(3)
            pyautogui.vscroll(-10)
            time.sleep(5)
            if find_and_click('img/telegram/clickbee-back.png'):
                time.sleep(5)
                continue

while True:
    if find_and_click('img/telegram/clickbee-visit-sites.png'):
        time.sleep(3)
        if find_and_click('img/telegram/clickbee-open-the-link.png'):
            time.sleep(3)
            if find_and_click('img/telegram/clickbee-open.png'):
                time.sleep(20)
                # wmctrl -l | grep -i chrome | cut -d' ' -f 1
                # xdotool windowunmap - hide window
                browser_window_id = os.system("wmctrl -l | grep -i chrome | cut -d' ' -f 1")
                os.system("xdotool windowunmap " + browser_window_id)
                time.sleep(3)
            else:
                print("Failed to open the link")
                exit(1)
        else:
            print("Can't open the link - no button")
            exit(2)
    else:
        print("Can't visit sites - no button")



