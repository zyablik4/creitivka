#Для правильной работы кода создайте 2 текстовых документа с названиями: "q.txt" и "s.txt, и запишите в q.txt своё имя, а в s.txt свою фамилию.
f = open('s.txt', 'r', encoding='utf-8')
w = f.read()
g = open('q.txt', 'r', encoding='utf-8')
q = g.read()
print('Здравтсвуйте', q, w+'!')
f.close()
g.close


