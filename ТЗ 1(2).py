import turtle
a = input('Введите цвет верхнего круга(на англ языке)')
s = input('Введите цвет среднего круга(на англ языке)')
d = input('Введите цвет нижнего круга(на англ языке)')
turtle.forward(150)
turtle.right(90)
turtle.forward(270)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(270)
turtle.penup()
print(turtle.pos())


turtle.goto(120,-45)
turtle.fillcolor(a)
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

turtle.goto(120,-135)
turtle.fillcolor(s)
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()

turtle.goto(120,-225)
turtle.fillcolor(d)
turtle.begin_fill()
turtle.circle(45)
turtle.end_fill()






