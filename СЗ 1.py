import turtle
a = input('Введите цвет верхнего круга(Цветов мало)')
s = input('Введите цвет среднего круга(Цветов мало)')
d = input('Введите цвет нижнего круга(Цветов мало)')
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.penup()
print(turtle.pos())
turtle.goto(120,-45)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()





