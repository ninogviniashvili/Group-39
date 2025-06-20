from turtle import *

#we want to paint a house

#step one:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,120)
pendown()

color("brown")
right(60)
forward(200)
right(90)
forward(80)
right(90)
forward(200)
right(90)
forward(80)
right(90)
forward(100)
color("green")
right(90)
forward(80)

penup()
goto(200,160)
pendown()

left(90)
forward(200)





exitonclick()