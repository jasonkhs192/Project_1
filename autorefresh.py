import pyautogui
import time
import os

os.system("start \"\" http://210.105.97.17/SLKPI/KPI_STATUS.aspx")
while True:
    time.sleep(1800)
    pyautogui.hotkey('ctrl', 'r')
