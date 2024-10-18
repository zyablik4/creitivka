#Для правильной работы кода создайте 3 текстовых документов: "q.txt" , "s.txt" и "e.txt", в "q.txt" запишите название устройства, в "s.txt" его предназначение и в "e.txt" его особые приметы.


f = open('s.txt', 'r', encoding='utf-8')
s = f.read()
f.close
g = open('q.txt', 'r', encoding='utf-8')
q = g.read()
h = open('e.txt', 'r', encoding='utf-8')
e = h.read()
h.close()
g.close()
f.close()

print('Название:', q)
print('Предназначение:', s)
print('Особые приметы:', e)
