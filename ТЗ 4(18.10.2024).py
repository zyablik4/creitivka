#Для правильной работы кода создайте 3 текстовых документов: "q.txt" , "s.txt" и "e.txt", запишите в них текст, который хотели бы сложить по такой схеме: "q.txt" + "s.txt" = "e.txt".


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

print(q, '+', s, '=', e)