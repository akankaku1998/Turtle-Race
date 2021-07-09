from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?\nColors: red, blue, yellow, green, purple\nEnter a color:")
race_start = False

turtle_list = []
x = -230
y = -80
color = ["red", "blue", "yellow", "green", "purple"]
for i in range(0, 5):
  k = Turtle(shape="turtle")
  k.penup()
  k.color(color[i])
  k.goto(x, y)
  y += 30
  turtle_list.append(k)
    

if user_input:
  race_start = True


while race_start:
  for turtle in turtle_list:
    if turtle.xcor() > -x:
      race_start = False
      win = turtle.pencolor()
      if win == user_input:
        print(f"You've won! The {win} turtle is the winner!")
      else:
        print(f"You've lost! The {win} turtle is the winner!")
    turtle.forward(random.randint(0, 10))


screen.exitonclick()
