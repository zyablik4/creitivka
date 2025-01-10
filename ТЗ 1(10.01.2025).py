import pyautogui as p
import keyboard as k
import time
a = input('Введите логин.')
s = input('Введите пароль.')
if a == '123' and s!= '1234':
    print('Пароль неверен')
if a != '123' and s == '1234':
    print('Логин неверен')
if a != '123' and s != '1234':
    print('Логин и пароль неверны')
if a == '123' and s == '1234':
    print('Успешный вход')
    p.press('win')
    time.sleep(1)
    k.write('секретные данные')
    time.sleep(1)
    p.press('enter')