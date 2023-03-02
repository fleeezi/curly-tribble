from ahk import AHK
import time

ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe')


def click():
    while True:
        time.sleep(1)
        ahk.right_click()
click()
