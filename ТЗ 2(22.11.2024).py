import pyautogui as p
import keyboard
import time
a = int(input('Выберите 1 или 2.'))
if a == 1:
    p.press('win')
    time.sleep(1)
    p.write('google chrome')
    time.sleep(1)
    p.moveTo(147, 362)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.write('hfpevty kb z?')
    time.sleep(1)
    p.press('enter')
if a == 2:
    p.press('win')
    time.sleep(1)
    p.write('google chrome')
    time.sleep(1)
    p.moveTo(147, 362)
    time.sleep(1)
    p.click()
    time.sleep(1)
    p.write('Ckfdf hj,jnfv!')
    time.sleep(1)
    p.press('enter')
