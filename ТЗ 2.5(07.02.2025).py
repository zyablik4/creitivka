import turtle as t
f = open('123.txt', 'r', encoding="utf-8")
f1 = open('1234.txt', 'w', encoding="utf-8")
str1 = f.readline().strip()
str2 = f.readline().strip()
str3 = f.readline().strip()
str4 = f.readline().strip()
str5 =f.readline().strip()
str6 = f.readline().strip()
t.speed(1)
if str2 == 'left':
    t.left(45)
if str2 == 'right':
    t.right(45)
if str2 == 'forward':
    t.forward(int(str1))

if str3 == 'left':
    t.left(45)
if str3 == 'right':
    t.right(45)
if str3 == 'forward':
    t.forward(int(str1))
    
if str4 == 'left':
    t.left(45)
if str4 == 'right':
    t.right(45)
if str4 == 'forward':
    t.forward(int(str1))
    
if str5 == 'left':
    t.left(45)
if str5 == 'right':
    t.right(45)
if str5 == 'forward':
    t.forward(int(str1))
    
if str6 == 'left':
    t.left(45)
if str6 == 'right':
    t.right(45)
if str6 == 'forward':
    t.forward(int(str1))
q = f1.write('Черепашка прошла по указанному пути с шагом в '+str1)
f.close()
f1.close()