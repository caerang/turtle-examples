import turtle

def square():
    kkobugi = turtle.Pen()
    kkobugi.shape("turtle")

    kkobugi.forward(100)
    kkobugi.left(90)
    kkobugi.forward(100)
    kkobugi.left(90)
    kkobugi.forward(100)
    kkobugi.left(90)
    kkobugi.forward(100)
    kkobugi.left(90)

def square_loop():
    kkobugi = turtle.Pen()
    kkobugi.shape("turtle")

    for i in range(4):
        kkobugi.forward(100)
        kkobugi.left(90)

if __name__ == '__main__':
    # square()
    square_loop()

    turtle.mainloop()
