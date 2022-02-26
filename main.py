# turtle drawing using circles
# yara elsakka
# 260222

import turtle as tu

tiddels         = tu.Turtle()  # Turtle object
window          = tu.Screen()  # Screen Object

window.bgcolor("black")        # Screen Bg color
window.title("Fractal Tree Pattern using Circles")

tiddels.left(90)        # moving the turtle 90 degrees towards left
tiddels.speed(20)       # setting the speed of the turtle

def draw(l):            # recursive function taking length 'l' as argument
    if (l < 10):
        print("draw nothing")
        return
    else:
        tiddels.pensize(2)              # Setting Pensize
        tiddels.pencolor("white")       # Setting Pencolor as yellow
        tiddels.forward(2*l)            # moving turtle forward by 2 x 'l'
        tiddels.left(30)                # moving the turtle 30 degrees towards left
        draw(l * (3 / 4))               # drawing a fractal on the left of the turtle object 'tiddels' with 3/4th of its length
        tiddels.circle(l)               # drawing circles with radius = l
        tiddels.right(60)               # moving the turtle 60 degrees towards right
        draw(l * (3 / 4))               # drawing a fractal on the right of the turtle object 'tiddels' with 3/4th of its length
        tiddels.circle(-l)              # drawing circles with radius = -l
        tiddels.left(30)                # moving the turtle 30 degrees towards left
        tiddels.backward(2*l)           # returning the turtle back to its original psition

draw(50)  # drawing 20 times



####################################
#
#tiddels.right(90)
#tiddels.speed(2000)
#
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("magenta")  # magenta
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(3 * l / 4)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(3 * l / 4)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.backward(l)
#
#draw(20)
#
##
#tiddels.left(270)
#tiddels.speed(2000)
##
#
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("red")  # red
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(3 * l / 4)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(3 * l / 4)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
##
##
#draw(20)
##
#tiddels.right(90)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("black")  # white #FFF8DC
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(3 * l / 4)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(3 * l / 4)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
##
#draw(20)
##
##########################################################
##
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(3)
#        tiddels.pencolor("lightgreen")  # lightgreen
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(4 * l / 5)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(4 * l / 5)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(3)
#        tiddels.backward(l)
##
#draw(40)
##
#tiddels.right(90)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(3)
#        tiddels.pencolor("red")  # red
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(4 * l / 5)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(4 * l / 5)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(3)
#        tiddels.backward(l)
##
#draw(40)
##
#tiddels.left(270)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(3)
#        tiddels.pencolor("yellow")  # yellow
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(4 * l / 5)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(4 * l / 5)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(3)
#        tiddels.backward(l)
##
#draw(40)
##
#tiddels.right(90)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(3)
#        tiddels.pencolor('#FFF8DC')  # white
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(4 * l / 5)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(4 * l / 5)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(3)
#        tiddels.backward(l)
#
#draw(40)
##
##########################################################
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("cyan")  # cyan
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(6 * l / 7)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(6 * l / 7)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
#
#draw(60)
##
#tiddels.right(90)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("yellow")  # yellow
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(6 * l / 7)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(6 * l / 7)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
##
#draw(60)
##
#tiddels.left(270)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor("magenta")  # magenta
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(6 * l / 7)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(6 * l / 7)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
##
#draw(60)
##
#tiddels.right(90)
#tiddels.speed(2000)
##
### recursion
#def draw(l):
#    if (l < 10):
#        return
#    else:
#        tiddels.pensize(2)
#        tiddels.pencolor('#FFF8DC')  # white
#        tiddels.forward(l)
#        tiddels.left(30)
#        draw(6 * l / 7)
#        tiddels.circle(l / 6)
#        tiddels.right(60)
#        draw(6 * l / 7)
#        tiddels.circle(-l / 6)
#        tiddels.left(30)
#        tiddels.pensize(2)
#        tiddels.backward(l)
##
#draw(60)

window.exitonclick()

# end of code 260222