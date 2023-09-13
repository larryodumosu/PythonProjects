from turtle import Turtle

ayesha = Turtle()
ayesha.color("Red")
ayesha.shape("turtle")

ayesha.penup()
ayesha.goto(-160, 100)
ayesha.pendown()

input("Press Enter to close")

ivo = Turtle
ivo.color("blue")
ayesha.penup()
ayesha.goto(-160, 70)
ayesha.pendown()

liam = Turtle()
liam.colo("brown")
ayesha.penup()
ayesha.goto(-160, 40)
ayesha.pendown()

from ramdom import randint

for movement in range(100):
  ayesha.forward(randint(1, 5))
  ivo.forward(randint(1, 5))
  liam.forward(randint(1, 5))

input("Press Enter to close")
