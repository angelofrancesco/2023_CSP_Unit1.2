# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
test = trtl.Turtle()
spot = test



#-----game configuration----
spot.speed(100)
spot.shape("circle")
spot.shapesize(5)
spot.fillcolor("pink")

#-----initialize turtle-----
def spot_onclick():


spot.onclick("circle")

#-----game functions--------
def spot_clicked(x, y):
    print("Spot was clicked!")

#-----events----------------

wn = trtl.Screen()
wn.mainloop()