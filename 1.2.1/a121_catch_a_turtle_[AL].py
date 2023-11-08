# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

test1 = trtl.Turtle()



#-----game configuration----
spot = test1
spot.speed(100)
spot.fillcolor("pink")
def drawSquare():
    spot.pendown()
    spot.fd(50)
    spot.right(90)
    spot.fd(50)
    spot.right(90)
    spot.fd(50)
    spot.right(90)
    spot.fd(50)

def drawTriangle(long, x, y):
    test.penup()
    test.goto(x, y)
    test.pendown()
    test.fd(long)
    test.right(90)
    test.fd(long)
    test.right(90)
    test.fd(long)
    test.right(90)
    test.fd(long)

x = -100
y = -100
length = 43
for tri in range(100):
    drawTriangle(length, x, y )
    x += length * 0.25
    y += length * 0.25
    length += 0.5

#-----initialize turtle-----


#-----game functions--------


#-----events----------------

wn = trtl.Screen()
wn.mainloop()