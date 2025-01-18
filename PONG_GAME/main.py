import turtle
import winsound

wn=turtle.Screen()
wn.title("PONG by @Shishir")
wn.bgcolor("green")
wn.setup(width=800,height=600)
wn.tracer(0)

#To draw middle line
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

draw_middle_line()

#Paddle A
paddle_a=turtle.Turtle()   #turtle module ko turtle class
paddle_a.speed(0)     #sets animation speed to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)   #centrepoint of this shape will be at this point
score_a=0

#Paddle B
paddle_b=turtle.Turtle()   #turtle module ko turtle class
paddle_b.speed(0)     #sets animation speed to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
score_b=0

#Ball
#ball is of 20*20 pixels
ball=turtle.Turtle()   #turtle module ko turtle class
ball.speed(0)     #sets animation speed to max
ball.shape("square")
ball.color("white")
# ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.5   
ball.dy=0.4   #everytime the ball moves,it moves by 2 pixels either on x or y axis

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()

is_running=False #initially keeping false

# Start menu music
def play_intro_music():
    winsound.PlaySound("PONG_GAME/intromusic.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

# Stop any currently playing music
def stop_music():
    winsound.PlaySound(None, winsound.SND_ASYNC)

#starting menu of game
def show_start_menu():
    play_intro_music()
    global is_running
    pen.clear()
    pen.goto(0, 100)
    pen.write("Welcome to Pong!", align="center", font=("impact", 30, "bold"))
    pen.goto(0, 0)
    pen.write(" 1. Start", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-30)
    pen.write("  2. Levels", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-60)
    pen.write("3. Help", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-90)
    pen.write("4. Quit", align="center", font=("courier", 20, "normal"))
    is_running = False  # Keep the game paused until Enter is pressed

#display levels
def levels():
    play_intro_music()
    pen.clear()
    pen.goto(0,60)
    pen.write("⚫ Level 1", align="center", font=("courier", 20, "normal"))
    pen.goto(0,20)
    pen.write("⚫ Level 2", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-20)
    pen.write("⚫ Level 3", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-60)
    pen.write("⚫ Level 4", align="center", font=("courier", 20, "normal"))
    pen.goto(0,-100)
    pen.write("⚫ Level 5", align="center", font=("courier", 20, "normal"))
    pen.goto(200,250)
    pen.write("Press 'b' to go back.",font=("ariel",13,"normal"))

#Help section
def help():
    global is_running
    play_intro_music()
    pen.clear()
    pen.goto(0,-100)
    pen.write("""              Welcome to the classic Pong game! The objective is simple: 
              keep the ball in play and score points by making it past your 
              opponent’s paddle. The game is played by two players. Player A 
              controls the paddle on the left side of the screen using the "W"
              key to move up and the "S" key to move down. Player B controls
              the paddle on the right side of the screen using the "Up Arrow"
              key to move up and the "Down Arrow" key to move down. The ball 
              will bounce off the paddles and the top and bottom edges of the 
              screen, but if it crosses your paddle, your opponent scores a 
              point. The first player to reach 7 points wins the game. Press 
              "r" to restart the game or "q" to quit at any time. Good luck 
              and have fun!""",align="center",font=("ariel",15,"normal"))
    pen.goto(200,250)
    pen.write("Press 'b' to go back.",font=("ariel",13,"normal"))
    is_running=False

#to officially start playing the game
def start_game():
    global is_running
    is_running = True
    stop_music()
    pen.clear()
    scoring(0, 0)  # Reset score
    main_game_loop()  # Start the main game loop

def scoring(sa,sb):
    pen.goto(0,260)
    pen.clear()
    pen.write(f"Player A : {sa}   Player B : {sb}",align="center",font=("Arial",24,"normal"))
    if (sa==7):
        global is_running
        winsound.PlaySound("PONG_GAME/winner.wav",winsound.SND_ASYNC)
        pen.goto(0,0)
        pen.write("Player A wins.",align="center",font=("Georgia",40,"normal"))
        pen.goto(0,-50)
        pen.write("Press 'r' to Restart or 'q' to Quit.",align="center",font=("verdana",20,"normal"))
        is_running=False
    elif (sb==7):
        winsound.PlaySound("PONG_GAME/winner.wav",winsound.SND_ASYNC)
        pen.goto(0,0)
        pen.write("Player B wins.",align="center",font=("Georgia",40,"normal"))
        pen.goto(0,-50)
        pen.write("Press 'r' to Restart or 'q' to Quit.",align="center",font=("verdana",20,"normal"))
        is_running=False

scoring(0,0)

#Moving the paddle
def paddle_a_up():
    y=paddle_a.ycor()
    if y<240:
        y+=20
        paddle_a.sety(y)   #set the value of y to new y's value

def paddle_a_down():
    y=paddle_a.ycor()
    if y>-240:
        y-=20
        paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    if y<240:
        y+=20
        paddle_b.sety(y)   #set the value of y to new y's value

def paddle_b_down():
    y=paddle_b.ycor()
    if y>-240:
        y-=20
        paddle_b.sety(y)

def restart_game():
    global score_a, score_b, is_running
    score_a, score_b = 0, 0
    ball.goto(0, 0)
    ball.dx, ball.dy = 0.4, 0.3
    pen.clear()
    pen.goto(0,260)
    scoring(score_a, score_b)
    is_running = True
    main_game_loop()

def quit_game():
    wn.bye()        #Closes the game window

#Keyboard binding
wn.listen()         #listens to any keyboard input
wn.onkeypress(paddle_a_up,"w")    #call the fxn when pressed "w"
wn.onkeypress(paddle_a_down,"s")  #call the fxn when pressed "s"
wn.onkeypress(paddle_b_up,"Up")    
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(restart_game,"r")
wn.onkeypress(quit_game,"q")
wn.onkeypress(start_game,"1")
wn.onkeypress(levels,"2")
wn.onkeypress(help,"3")
wn.onkeypress(quit_game,"4")
wn.onkeypress(show_start_menu,"b")

#Main game loop
def main_game_loop():
    global is_running
    global score_a,score_b
    while True:
        if is_running:
            wn.update()

            #Moving the ball
            ball.setx(ball.xcor() + ball.dx)    #current x cord. + 2 pixels movement ; starting =(0,0)
            ball.sety(ball.ycor() + ball.dy)    #current y cord. + 2 pixels movement

            #Border checking of ball
            if ball.ycor()>290:
                winsound.PlaySound("PONG_GAME/bounce02.wav",winsound.SND_ASYNC)
                ball.sety(290)
                ball.dy*=-1             #This reverses the direction

            if ball.ycor()<-290:
                winsound.PlaySound("PONG_GAME/bounce02.wav",winsound.SND_ASYNC)
                ball.sety(-290)
                ball.dy*=-1  

            if ball.xcor()<-390:
                score_b+=1
                ball.goto(0,0)      #restart the game by putting ball in center
                ball.dx*=-1  
                scoring(score_a,score_b)

            if ball.xcor()>390:
                score_a+=1
                ball.goto(0,0)
                ball.dx*=-1 
                scoring(score_a,score_b)
            
            #Paddle and ball collisions
            if ball.xcor()>340 and ball.xcor()<343 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50:
                winsound.PlaySound("PONG_GAME/bounce01.wav",winsound.SND_ASYNC)
                ball.setx(340)
                ball.dx*=-1  

            if ball.xcor()<-340 and ball.xcor()>-343 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50:
                winsound.PlaySound("PONG_GAME/bounce01.wav",winsound.SND_ASYNC)
                ball.setx(-340)
                ball.dx*=-1

        else:
            wn.update()

#calling the loop
show_start_menu()
wn.mainloop()