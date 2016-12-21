import time
import turtle
t= turtle.Pen()
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##turtle.getscreen()._root.mainloop()
##
t.reset()

##estrella
##for x in range (1,9):
##    t.forward(100)
##    t.left(225)
a=7

for x in range (1,a+1):
    t.forward(100)


    an=180/a
    ang=180 - an
    t.left(ang)
turtle.getscreen()._root.mainloop()

