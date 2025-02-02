import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple','blue','green','orange','yellow']
s.bgcolor('pink')
t.speed('slow')
t.hideturtle()
while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
        t.right(239)
        for x in range(200, 0, -1):
            t.pencolor('white')
            t.width(x/100 +  7)
            t.forward(x)
            t.right(59)