import telnetlib
import turtle as t

from numpy import left_shift


#삼각형 그리기
# t.color("green")
# t.pensize(5)
# t.forward(120)
# t.left(140)
# t.forward(120)
# t.left(140)
# t.forward(120)
# t.left(140)
# t.forward(140)
# t.left(154.21)
# t.forward(140)
# t.done()


#원 그리기
#t.color('red')
#t.circle(10)
#t.forward(15)
#t.circle(15)
#t.forward(20)
#t.circle(20)
#t.forward(25)
# t.circle(25)
# t.done()


# t.color("red")
# t.forward(100)
# t.left(90)
# t.up()
# t.forward(100)
# t.left(90)
# t.down()
# t.forward(100)
# t.done()


t.pensize(7)
t.circle(50)
t.color('yellow')
t.left(90)
t.circle(50)
t.color('green')
t.right(180)
t.circle(50)
t.up()
t.left(90)
t.forward(110)
t.down()
t.color('red')
t.circle(50)
t.up()
t.right(180)
t.forward(219)
t.down()
t.color('blue')
t.right(180)
t.circle(50)
t.done()
