import subprocess
import time
from ahk import AHK

ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe')

files = ["main.py", "bot.py" , 'click.py']  # файлы, которые нужно запустить
for file in files:
    subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)
