import pyautogui as p
import keyboard
import time

a = input('Введите имя файла, который вы хотите открыть 1)бобр (1).jpeg 2)илья.JPG 3)noroot.png')
if int(a) == 1:
    p.moveTo(1766, 6)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(800, 750)
    time.sleep(1)
    p.doubleClick()
    
if int(a) == 2:
    p.moveTo(1766, 6)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(901, 23)
    time.sleep(1)
    p.doubleClick()
    
if int(a) == 3:
    p.moveTo(1766, 6)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.moveTo(626, 340)
    time.sleep(1)
    p.doubleClick()