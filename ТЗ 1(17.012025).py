f = open('123.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
str2 = f.readline().strip()
a = input('Введите логин.')
s = input('Введите пароль.')
if a == str1 and s == str2:
    print('Успешный вход!')
else:
    print('Логин или пароль неверный!')
f.close()