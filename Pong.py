

import turtle

wn = turtle.Screen()
wn.title("IS THIS PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
player_a = 0
player_b = 0


# Slider 1
slider_1 = turtle.Turtle()
slider_1.speed(0)
slider_1.shape("square")
slider_1.color("white")
slider_1.shapesize(stretch_wid=5, stretch_len=1)
slider_1.penup()
slider_1.goto(-350, 0)

# Slider 2
slider_2 = turtle.Turtle()
slider_2.speed(0)
slider_2.shape("square")
slider_2.color("white")
slider_2.shapesize(stretch_wid=5, stretch_len=1)
slider_2.penup()
slider_2.goto(+350, 0)


# Pong Ball
pball = turtle.Turtle()
pball.speed(0)
pball.shape("square")
pball.color("white")
pball.penup()
pball.goto(0, 0)
pball.dx = 0.2
pball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 25, "normal"))

# Working Function
def slider1_up():
    y = slider_1.ycor()
    y += 20
    slider_1.sety(y)


def slider1_down():
    y = slider_1.ycor()
    y -= 20
    slider_1.sety(y)


def slider2_up():
    y = slider_2.ycor()
    y += 20
    slider_2.sety(y)


def slider2_down():
    y = slider_2.ycor()
    y -= 20
    slider_2.sety(y)

# Key Binds
wn.listen()
wn.onkeypress(slider1_up, "w")
wn.onkeypress(slider1_down, "s")

wn.onkeypress(slider2_up, "Up")
wn.onkeypress(slider2_down, "Down")



# Game loop main
while True:
    wn.update()

    # moving the ball
    pball.setx(pball.xcor() + pball.dx)
    pball.sety(pball.ycor() + pball.dy)

    # border check top & bottom
    if pball.ycor() > 290:
        pball.sety(290)
        pball.dy *= -1

    if pball.ycor() < -290:
        pball.sety(-290)
        pball.dy *= -1

    # border check side to side

    if pball.xcor() > 390:
        pball.goto(0, 0)
        pball.dx *= -1
        player_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(player_a, player_b), align="center", font=("Courier", 25, "normal"))

    if pball.xcor() < -390:
        pball.goto(0, 0)
        pball.dx *= -1
        player_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(player_a, player_b), align="center", font=("Courier", 25, "normal"))

    # ball collision
    # basically checks if the ball is b/w the slider and border & if the ball is hitting the slider

    if (pball.xcor() > 340 and pball.xcor() < 350) and (pball.ycor() < slider_2.ycor() + 50 and pball.ycor() > slider_2.ycor()-50):
        pball.setx(340)
        pball.dx *= -1

    if (pball.xcor() < -340 and pball.xcor() > -350) and (pball.ycor() < slider_1.ycor() + 50 and pball.ycor() > slider_1.ycor()- 50):
        pball.setx(-340)
        pball.dx *= -1




