import turtle
import random

t = turtle.Turtle()
t.speed(40)
# Turn off animation initially

def draw_square(x, y, distance, color, fillcolor):
    t.color(color)
    t.fillcolor(fillcolor)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(distance)
        t.left(90)
    t.end_fill()

def draw_circle(x, y, radius, color, fillcolor):
    t.color(color)
    t.fillcolor(fillcolor)
    t.penup()
    t.setposition(x, y - radius)  # Adjust position to start from the top
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_triangle(x, y, distance, color, fillcolor):
    t.color(color)
    t.fillcolor(fillcolor)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(distance)
        t.left(120)
    t.end_fill()

def draw_shapes(shape_function, num_shapes, size_range, color1, color2):
    for _ in range(num_shapes):
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        size = random.randint(*size_range)
        shape_function(x, y, size, color1, color2)
        turtle.update()  # Update the screen for each shape

turtle.hideturtle()  # Hide the default turtle

# Draw squares
draw_shapes(draw_square, random.randint(1, 4), (50, 100), "blue", "lightblue")

# Draw circles
draw_shapes(draw_circle, 5, (50, 75), "red", "pink")

# Draw triangles
draw_shapes(draw_triangle, random.randint(1, 4), (40, 80), "green", "lightgreen")

turtle.done()  # Finish the drawing process
