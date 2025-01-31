import pyautogui as p
import time
import keyboard as k
f = open('123.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
str2 = f.readline().strip()
p.press('win')
time.sleep(0.5)
p.write(str1)
time.sleep(0.5)
p.press('enter')
time.sleep(1)
k.write(str2)
time.sleep(0.5)
p.press('enter')
f.close()