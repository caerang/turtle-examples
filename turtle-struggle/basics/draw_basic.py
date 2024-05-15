import turtle

kkobugi = turtle.Turtle()

# 원 그리기
kkobugi.color('blue')
kkobugi.pensize(5)
kkobugi.up()
kkobugi.forward(50)
kkobugi.down()
kkobugi.circle(60)

kkobugi.speed(1)
kkobugi.forward(20)
kkobugi.left(-90)
kkobugi.right(90)
kkobugi.left(30)

turtle.mainloop()