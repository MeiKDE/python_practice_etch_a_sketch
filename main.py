from turtle import Turtle, Screen

# create a turtle object
t = Turtle()
screen = Screen()


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
    t.home()  # move turtle to home position
    t.pendown()  # put pen down to start drawing again


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)  # turn left
screen.onkey(key="d", fun=clockwise)  # turn right
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
