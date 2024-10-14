# Turtle Drawing Program

This is a simple Turtle Graphics program that allows users to control the movement of a turtle using keyboard keys. The turtle can move forward, backward, rotate left, rotate right, and clear its drawing.

## Features

- Move the turtle forward and backward.
- Rotate the turtle clockwise and counterclockwise.
- Clear the turtle's drawing and reset it to the home position.

## How to Use

The turtle is controlled using the following keys:

- **W**: Move the turtle forward by 10 units.
- **S**: Move the turtle backward by 10 units.
- **A**: Rotate the turtle counterclockwise by 10 degrees.
- **D**: Rotate the turtle clockwise by 10 degrees.
- **C**: Clear the drawing and reset the turtle to the center.

## Code Overview

```python
from turtle import Turtle, Screen

# create a turtle object
t = Turtle()
screen = Screen()

# Functions for controlling the turtle
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def counter_clockwise():
    new_heading = t.heading() + 10  # or use left() function
    t.setheading(new_heading)

def clockwise():
    new_heading = t.heading() - 10  # or use right() function
    t.setheading(new_heading)

def clear_drawing():
    t.clear()  # clear turtle drawing not screen
    t.penup()  # lift pen up to not draw
    t.home()   # move turtle to home position
    t.pendown()  # put pen down to start drawing again

# Set up the screen to listen for key presses
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)  # turn left
screen.onkey(key="d", fun=clockwise)  # turn right
screen.onkey(key="c", fun=clear_drawing)

# Exit on click
screen.exitonclick()
