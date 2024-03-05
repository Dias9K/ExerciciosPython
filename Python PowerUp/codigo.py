#p.hotkey('win', 'e')
import pyautogui as p
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
p.PAUSE = 1
p.press("win")
p.write("edge")
p.press("enter") 
p.write(link)
p.press("enter") 
time.sleep(3)

p.click(x=707, y=359) # email
p.click(x=716, y=454) # senha