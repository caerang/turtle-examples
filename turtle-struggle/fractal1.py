import turtle

kkobugi = turtle.Turtle()

kkobugi.speed(6)

kkobugi.getscreen().bgcolor("black")
kkobugi.color("cyan")

kkobugi.penup()
kkobugi.goto((-200, 50))
kkobugi.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

if __name__ == '__main__':
    star(kkobugi, 360)
    turtle.mainloop()
