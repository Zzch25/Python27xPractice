#Zachary Job
#10/9/12

import turtle

#########
#turtle.
#########
#forward() 
#backward()
#right()
#left()
#degrees()
#penup()
#pendown()
#isdown()
#reset()
#goto()
#setheading()

turn = 15
turtle.degrees()

def reset():
    return turtle.reset()

def exit():
    return turtle.bye()

#svTree(400, 5)
#Via print statements, I found that a slower refresh rate causes the code to
#work properly. I have no idea why, but I assume that maybe turtle is glitchy.
#Without the print statements, I believe it will error as it does above 5 levels
#around 3 or 4. To my knowledge, the logic seems fine.

def svTree(tlen, levels):
    if tlen == [] or levels == [] or tlen == 0 or levels == 0:
        return "Bad Input"
    if turtle.pos() == (0.0,0.0):
        turtle.setheading(90)
        turtle.forward(-tlen)
        turtle.forward(tlen)
    if levels > 1:
        turtle.setheading((turtle.heading())+turn)
        print "turn + "
        print turtle.heading()
        print "forward + "
        print tlen/2
        turtle.forward(tlen/2)
        svTree(tlen/2, levels - 1)
        print "backwards - "
        print tlen/2
        turtle.forward(-tlen/2)
        turtle.setheading((turtle.heading())-turn*2)
        print "turn -- "
        print turtle.heading()
        print "forward + "
        print tlen/2
        turtle.forward(tlen/2)
        svTree(tlen/2, levels - 1)
        print "backwards - "
        print tlen/2
        turtle.forward(-tlen/2)
        turtle.setheading((turtle.heading())+turn)
        print "turn + "
        print turtle.heading()
        print "====Position===="
        print turtle.pos()
        print "================"
        

print svTree(400, 5)

    

