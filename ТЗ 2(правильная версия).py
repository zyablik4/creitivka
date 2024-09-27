import turtle
a = turtle.textinput('Гена', 'Какой хотите цвет одежды гены?')
s = turtle.textinput('Чебурашка', 'Какой хотите цвет шерсти чебурашки')

turtle.fillcolor('green')
turtle.begin_fill()

turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

turtle.right(180)
turtle.forward(50)

turtle.fillcolor('white')
turtle.begin_fill()

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()

turtle.left(90)
turtle.forward(50)

turtle.fillcolor(a)
turtle.begin_fill()

turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()

turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.fillcolor('green')
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()

turtle.penup()
turtle.goto(100,-150)
turtle.pendown()

turtle.fillcolor(s)
turtle.begin_fill()

turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.end_fill()

turtle.right(90)
turtle.forward(50)

turtle.fillcolor('Khaki')
turtle.begin_fill()

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

turtle.end_fill()

turtle.forward(50)

turtle.fillcolor(s)
turtle.begin_fill()

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.end_fill()

turtle.right(180)
turtle.forward(50)

turtle.fillcolor(s)
turtle.begin_fill()

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.end_fill()

turtle.penup()
turtle.goto(65,20)
turtle.write('Гена')

turtle.goto(150,-130)
turtle.write('Чебурашка')





