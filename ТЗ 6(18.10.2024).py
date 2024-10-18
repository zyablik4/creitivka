#Для правильной работы кода создайте 3 текстовых документов: "q.txt" , "s.txt" и "e.txt", в "q.txt" запишите стоимость одного кирпича, в "s.txt" стоимость 1 кг цемента и в "e.txt" стоимость 1 кг песка.
import time
print('Надо купить:')
time.sleep(1)
print('200 кирпичей')
time.sleep(1)
print('3 кг цемента')
time.sleep(1)
print('5 кг песка')
time.sleep(2)

f = open('s.txt', 'r', encoding='utf-8')
s = f.read()
g = open('q.txt', 'r', encoding='utf-8')
q = g.read()
h = open('e.txt', 'r', encoding='utf-8')
e = h.read()
h.close()
g.close()
f.close()

q = int(q)
s = int(s)
e = int(e)
print('Исходя по вами записанными данными общая сумма равна:', q*200+s*3+e*5, 'рублей!')

