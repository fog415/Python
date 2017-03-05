import turtle
import math
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(bob,100)

def polygon(t,n,length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(bob,100,10)

def circle(t,r):
    polygon(bob,360,2*math.pi*r/360)

#circle(bob,50)

def arc(t,r,angle):
    for i in range(angle):
        t.fd(2*math.pi*r/360)
        t.lt(1)

arc(bob,50,90)

turtle.mainloop()     # This command must be the last statement !
