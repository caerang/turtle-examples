import turtle

t = turtle.Turtle()

def tree(length):
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length-15)
        t.left(20)
        tree(length-15)
        t.right(20)
        t.backward(length)
    else:
        t.forward(length)

t.left(90)
t.color("green")
t.speed(1)
tree(90)
turtle.mainloop()