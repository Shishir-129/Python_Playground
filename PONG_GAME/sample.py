import turtle
import winsound

# Initialize window
wn = turtle.Screen()
wn.title("Pong by Mr_Hawks")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()  # turtle module ko turtle class
paddle_a.speed(0)  # sets animation speed to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)  # centerpoint of this shape will be at this point
score_a = 0

# Paddle B
paddle_b = turtle.Turtle()  # turtle module ko turtle class
paddle_b.speed(0)  # sets animation speed to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
score_b = 0

# Ball
# ball is of 20*20 pixels
ball = turtle.Turtle()  # turtle module ko turtle class
ball.speed(0)  # sets animation speed to max
ball.shape("square")
ball.color("white")
# ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.3  # every time the ball moves, it moves by 2 pixels either on x or y axis

# Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

is_running = False  # Set to False initially until the game starts


# Function to draw the middle line
def draw_middle_line():
    middle_line = turtle.Turtle()
    middle_line.speed(0)
    middle_line.color("white")
    middle_line.penup()
    middle_line.goto(0, 300)  # Start at the top of the screen
    middle_line.setheading(270)  # Point the turtle downwards
    middle_line.pendown()
    middle_line.goto(0, -300)  # Draw the line to the bottom of the screen
    middle_line.hideturtle()


# Function to display the start menu
def show_start_menu():
    global is_running
    pen.clear()
    pen.goto(0, 100)
    pen.write("Welcome to Pong!", align="center", font=("Courier", 30, "normal"))
    pen.goto(0, 0)
    pen.write("Press Enter to Start, Q to Quit", align="center", font=("Courier", 20, "normal"))
    is_running = False  # Keep the game paused until Enter is pressed


# Function to start the game
def start_game():
    global is_running
    is_running = True
    pen.clear()
    scoring(0, 0)  # Reset score
    main_game_loop()  # Start the main game loop


# Function to quit the game
def quit_game():
    wn.bye()  # Closes the game window


# Function to update score
def scoring(sa, sb):
    pen.clear()
    pen.write(f"Player A : {sa}   Player B : {sb}", align="center", font=("Courier", 24, "normal"))
    if (sa == 7):
        global is_running
        pen.goto(0, 0)
        pen.write("Player A wins.", align="center", font=("Courier", 40, "normal"))
        is_running = False
    elif (sb == 7):
        pen.goto(0, 0)
        pen.write("Player B wins.", align="center", font=("Courier", 40, "normal"))
        is_running = False


# Moving the paddle
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
        paddle_a.sety(y)  # set the value of y to new y's value


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
        paddle_b.sety(y)  # set the value of y to new y's value


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)


def restart_game():
    global score_a, score_b, is_running
    score_a, score_b = 0, 0
    ball.goto(0, 0)
    ball.dx, ball.dy = 0.4, 0.3
    pen.clear()
    scoring(score_a, score_b)
    is_running = True
    main_game_loop()


def quit_game():
    wn.bye()  # Closes the game window


# Keyboard binding
def setup_key_bindings():
    wn.listen()  # listens to any keyboard input
    wn.onkeypress(paddle_a_up, "w")  # call the fxn when pressed "w"
    wn.onkeypress(paddle_a_down, "s")  # call the fxn when pressed "s"
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    wn.onkeypress(start_game, "Return")  # Press "Enter" to start
    wn.onkeypress(quit_game, "q")  # Press "Q" to quit


# Main game loop
def main_game_loop():
    global is_running
    global score_a, score_b
    while is_running:
        wn.update()

        # Moving the ball
        ball.setx(ball.xcor() + ball.dx)  # current x cord. + 2 pixels movement ; starting =(0,0)
        ball.sety(ball.ycor() + ball.dy)  # current y cord. + 2 pixels movement

        # Border checking of ball
        if ball.ycor() > 290:
            winsound.PlaySound("PONG_GAME/bounce02.wav", winsound.SND_ASYNC)
            ball.sety(290)
            ball.dy *= -1  # This reverses the direction

        if ball.ycor() < -290:
            winsound.PlaySound("PONG_GAME/bounce02.wav", winsound.SND_ASYNC)
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() < -390:
            score_b += 1
            ball.goto(0, 0)  # restart the game by putting ball in center
            ball.dx *= -1
            scoring(score_a, score_b)

        if ball.xcor() > 390:
            score_a += 1
            ball.goto(0, 0)
            ball.dx *= -1
            scoring(score_a, score_b)

        # Paddle and ball collisions
        if ball.xcor() > 340 and ball.xcor() < 343 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            winsound.PlaySound("PONG_GAME/bounce01.wav", winsound.SND_ASYNC)
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -343 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            winsound.PlaySound("PONG_GAME/bounce01.wav", winsound.SND_ASYNC)
            ball.setx(-340)
            ball.dx *= -1


# Start the game with the menu
show_start_menu()  # Display the start menu
setup_key_bindings()  # Set up the key bindings for the menu and game
wn.mainloop()  # Start the turtle graphics loop
