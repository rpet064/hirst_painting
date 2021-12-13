#! Python 3
#hirst_painting.py
#this file makes my own Hirst dot painting - Please make full screen when running
import turtle as t
import random as r
color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),(139, 168, 195), (206, 154, 121), (192, 140, 150),(25, 36, 55)]
colormode = t.colormode(255)
#hide turtle
t.hideturtle()
#width of the pen to make dots
t.width(15)
#set the turtle's shape
t.shape("turtle")
#set the turtle's color
t.color("blue")
#to speed up runtime
t.speed("fastest")
#needs to repeat 10 rows
for i in range (10):
    y = -290
    #To reset position tp start of the row
    t.pu()
    t.setposition(-590, (y + 60 * i))
    for j in range(10):
        t.dot(40, r.choice(color_list))
        t.forward(55)
    #loop to make dots on each row
    #for r,b,g in color_list:
        #uses the list extracted from the painting for color

        #t.pencolor(r, g ,b)
        #t.pd()
        t.forward(70)
        #gap between dots
        #t.pu()
        #t.forward(55)


my_screen = t.Screen()
my_screen.exitonclick()