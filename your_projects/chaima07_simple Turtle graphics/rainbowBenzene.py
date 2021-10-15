#rainbow Benzene
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Turtle()
turtle.bgcolor('black')
for x in range(100):
    t.color(colors[x%6])
    t.forward(x)
    t.left(59)
turtle.done()
