import cv2
import numpy as np
import time
import mss
from ahk import AHK


ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe')


def screen_record_efficient() -> int:
    # 800x600 windowed mode
    mon = {"top": 200, "left": 600, "width": 800, "height": 150}
    title = "Castaways Bot"
    fps = 0
    sct = mss.mss()
    last_time = time.time()
    time.sleep(4)
    ahk.right_click()
    while True:


        img = np.asarray(sct.grab(mon))

        fps += 1

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)








        mask_yellow = cv2.inRange(hsv, (25, 220, 250), (32, 255, 255))
        mask_purple = cv2.inRange(hsv,(150, 100, 100) , (160, 255, 255) )

        mask_green = cv2.inRange(hsv, (50, 100, 240), (70, 255, 255))
        # if there are any white pixels on mask, sum will be > 0
        hasPurple = np.sum(mask_purple)
        hasYellow = np.sum(mask_yellow)

        hasGreen = np.sum(mask_green)
        if hasYellow > 0:
            print('Yellow detected!')
            time.sleep((0.07))
            ahk.key_press('up')
            time.sleep((0.29))
        elif hasPurple > 0:
            print('Purple Detected')
            time.sleep((0.07))
            ahk.key_press('left')
            time.sleep((0.2))
        elif hasGreen > 0:
            print('Green Detected')
            time.sleep((0.07))
            ahk.key_press('right')
            time.sleep((0.29))
        else:
            print('Nothing detected')
            time.sleep(0.2)



screen_record_efficient()


