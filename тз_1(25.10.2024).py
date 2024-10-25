s = input('Введите свою фамилию.')
a = input('Введите своё имя.')

file = open('dara.txt', 'w', encoding='utf-8')
file.write(a+' '+s)
#file.write(s)
file.close()


