from turtle import *
import random

colors= ["black","red"]
#bgcolor= "blue"

speed (1000)
for x in range (100):
    aleatorio= random.randrange(0,2)
    pencolor(colors[aleatorio])
    width(x/50+1)
    #forward (x)
    circle(100)
    left(70)

hideturtle()
done()