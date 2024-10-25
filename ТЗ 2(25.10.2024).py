s = input('Введите первое слово.')
a = input('Введите второе слово.')

file = open('dara.txt', 'w', encoding='utf-8')
file.write(a)

f_file = open('data.txt', 'w', encoding='utf-8')
f_file.write(s)

#q_file = open('data.txt', 'r', encoding='utf-8')
#q_file.read(s)

file.write(a+' '+s)

file.close()
f_file.close()