#Для правильной работы кода создайте 3 текстовых документов: "q.txt" , "s.txt" и "e.txt", в "q.txt" запишите кол-во кроликов белой породы, в "s.txt" кол-во кроликов розовой породы и в "e.txt" кол-во кроликов коричневой породы.
#Создайте ещё 3 текстовых документа с названиями: "z.txt", "x.txt" и "c.txt", в "z.txt" запишите стоимость за одного кролика белой породы, в "x.txt" стоимость за одного кролика розовой породы и в "c.txt" стоимость за одного кролика коричневой породы.

import time

print('Викентий любит разводить кроликов, у него три породы: белые, коричневые и розовые.')
time.sleep(2)
f = open('s.txt', 'r', encoding='utf-8')
s = f.read()
g = open('q.txt', 'r', encoding='utf-8')
q = g.read()
h = open('e.txt', 'r', encoding='utf-8')
e = h.read()
j = open('z.txt', 'r', encoding='utf-8')
z = j.read()
k = open('x.txt', 'r', encoding='utf-8')
x = k.read()
l = open('c.txt', 'r', encoding='utf-8')
c = l.read()

l.close()
k.close()
j.close()
h.close()
g.close()
f.close()

q = int(q)
s = int(s)
e = int(e)
z = int(z)
x = int(x)
c = int(c)
print('Если Викентий продаст всех кроликов, то он получит:', q*z+s*x+e*c, 'рублей!')

