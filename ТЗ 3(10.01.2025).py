import pyautogui as p
import keyboard as k
import time
a = int(input('Введите текущую влажность в оранжерее'))
s = int(input('Введите текущую температуру в оранжерее'))
if a > 60 and s < 10 or a < 30 and s > 30:
    print('Тревога!')
    p.press('win')
    time.sleep(0.5)
    p.write('google')
    time.sleep(0.5)
    p.press('enter')
    time.sleep(0.5)
    k.write('что делать при нарушении условий в оранжерее')
    time.sleep(0.5)
    p.press('enter')
else:
    print('Всё нормально')