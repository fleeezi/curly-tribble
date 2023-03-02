import cv2
import numpy as np
import time
import mss
from ahk import AHK

ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe')
time.sleep(9)
def screen_record_efficient2() -> int:
    # 800x600 windowed mode

    mon2 = {"top": 270, "left": 865, "width": 60, "height": 12}
    title = "Castaways Bot"
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while True:
        img2 = np.asarray(sct.grab(mon2))
        hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        mask_blue = cv2.inRange(hsv, (85, 100, 100), (100, 255, 255))
        hasBlue = np.sum(mask_blue)
        if hasBlue > 0:
            print('Blue Detected')
            ahk.key_press('down')
            time.sleep(0.26)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


screen_record_efficient2()
