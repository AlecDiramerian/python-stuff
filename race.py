import turtle, random


setup = turtle.Pen()
r1 = turtle.Pen()
r2 = turtle.Pen()
r3 = turtle.Pen()
r4 = turtle.Pen()

setup.penup()
setup.goto(500, 200)
setup.pendown()
setup.pensize(10)
setup.right(90)
setup.forward(400)
setup.hideturtle()

r1.penup()
r2.penup()
r3.penup()
r4.penup()

r1.goto(-500, 20)
r2.goto(-500, -20)
r3.goto(-500, 50)
r4.goto(-500, -50)

while True:
    r1.fd(random.randint(1,10))
    r2.fd(random.randint(1,10))
    r3.fd(random.randint(1,10))
    r4.fd(random.randint(1,10))
    if r1.xcor() > 500:
        r1.goto(550, 20)
        break
    elif r2.xcor() > 500:
        r2.goto(550, -20)
        break
    elif r3.xcor() > 500:
        r3.goto(550, 50)
        break
    elif r4.xcor() > 500:
        r4.goto(550, -50)
        break 