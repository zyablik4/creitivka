#Для правильной работы кода создайте текстовые документы с названием dara.txt и data.txt,в dara.txt запишите строчку, которую хотели бы добавить в data.txt  

file = open('dara.txt', 'r', encoding='utf-8')
a = file.read()

f_file = open('data.txt', 'w', encoding='utf-8')
f_file.write(a)

file.close()
f_file.close()