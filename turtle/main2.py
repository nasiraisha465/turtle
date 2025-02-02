import turtle
turtle.Screen().bgcolor("yellow")
sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range (5):
    board.forward(100)
    board.left(144)
sc.mainloop()