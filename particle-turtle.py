import random
import turtle

RADIUS = 50

circle = turtle.Turtle()
circle.penup()
circle.setpos(circle.pos()[0], circle.pos()[1] - RADIUS)
circle.pendown()
circle.color("blue")
circle.circle(RADIUS)

particle = turtle.Turtle()
particle.color("red")

count = 0
while True:
    particle.forward(5)
    if random.randint(0, 1) == 0:
        particle.left(random.randint(0, 100))
    else:
        particle.right(random.randint(0, 100))
    if abs(particle.pos()[0]) >= RADIUS or abs(particle.pos()[1]) >= RADIUS:
        break
    count += 1

print(str(count))
