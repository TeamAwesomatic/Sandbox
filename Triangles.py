import turtle


def draw_triangle(size):
    turtle.rt(120)

    for i in range(4):
        turtle.fd(size)
        turtle.lt(120)

    turtle.fd(size / 2)


for j in range(1, 4):
    draw_triangle(10 * j)

raw_input('')
