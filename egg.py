import pyautogui
import time

pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("steam")
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(x=85, y=177)
pyautogui.write("egg")
pyautogui.click(x=60, y=243)
pyautogui.click(x=374, y=421)
time.sleep(3)
pyautogui.click(x=958, y=572, clicks=1000000, interval=0.03)