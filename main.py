from turtle import Turtle, Screen, addshape
import turtle
import random
import time
import winsound

s = 0.015
addshape(shape=None,name="right_submarine.gif")
addshape(shape=None,name="left_submarine.gif")
addshape(shape=None,name="up_submarine.gif")
addshape(shape=None,name="down_submarine.gif")
addshape(shape=None,name="oxygen.gif")
addshape(shape=None,name="mine.gif")
addshape(shape=None,name="start.gif")
addshape(shape=None,name="blow1.gif")
addshape(shape=None,name="blow2.gif")
addshape(shape=None,name="blow3.gif")
addshape(shape=None,name="blow4.gif")
addshape(shape=None,name="game_over.gif")

winsound.PlaySound("8-bitcut.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)


sc = Screen()
sc.title("Ocean Gate")
sc.tracer(0)
sc.setup(width=700,height=500)
time.sleep(0.2)
sc.bgpic("sea.gif")



#mines
mine1 = Turtle(shape="mine.gif")
mine1.penup()
mine2 = Turtle(shape="mine.gif")
mine2.penup()
mine3 = Turtle(shape="mine.gif")
mine3.penup()
mine4 = Turtle(shape="mine.gif")
mine4.penup()
bombs = [mine1,mine2,mine3,mine4]

#oxygen
oxy = Turtle(shape="oxygen.gif")
oxy.penup()
oxy.setpos(random.randint(-300,300), random.randint(-200,200))

def new_locations():
    mine1.setpos(random.randint(-300,0), random.randint(0,200))
    if sub.xcor() < mine1.xcor() + 39 and sub.xcor() > mine1.xcor() - 39 and sub.ycor() < mine1.ycor() + 39 and sub.ycor() > mine1.ycor() - 39:
        mine1.setpos(random.randint(-300,0), random.randint(0,200))
        
    mine2.setpos(random.randint(0,300), random.randint(0,200))
    if sub.xcor() < mine2.xcor() + 39 and sub.xcor() > mine2.xcor() - 39 and sub.ycor() < mine2.ycor() + 39 and sub.ycor() > mine2.ycor() - 39:
        mine2.setpos(random.randint(0,300), random.randint(0,200))
    
    mine3.setpos(random.randint(-300,0), random.randint(-200,0))
    if sub.xcor() < mine3.xcor() + 39 and sub.xcor() > mine3.xcor() - 39 and sub.ycor() < mine3.ycor() + 39 and sub.ycor() > mine3.ycor() - 39:
        mine3.setpos(random.randint(-300,0), random.randint(-200,0))
        
    mine4.setpos(random.randint(0,300), random.randint(-200,0))
    if sub.xcor() < mine4.xcor() + 39 and sub.xcor() > mine4.xcor() - 39 and sub.ycor() < mine4.ycor() + 39 and sub.ycor() > mine4.ycor() - 39:
        mine4.setpos(random.randint(0,300), random.randint(-200,0))
        
    oxy.setpos(random.randint(-300,300), random.randint(-200,200))


sub = Turtle(shape="right_submarine.gif")
sub.penup()

#start button
start_button = Turtle(shape="start.gif")
start_button.penup()

#score
score = Turtle()
score.hideturtle()
score.color("white")
scoring = 0
score.penup()
score.goto(0,210)
score.write(f"Score: {scoring}",align="Center", font=("Courier", 20, "normal"))


def new_score():
    global scoring
    score.clear()
    scoring += 1
    score.write(f"Score: {scoring}",align="Center", font=("Courier", 20, "normal"))
    
new_locations()

def check_oxy(sub,oxy):
    global s
    if sub.xcor() < oxy.xcor() + 9 and sub.xcor() > oxy.xcor() - 9 and sub.ycor() < oxy.ycor() + 21 and sub.ycor() > oxy.ycor() - 25:
        s *= .97
        winsound.PlaySound("get_oxy.wav", winsound.SND_ASYNC)
        new_score()
        new_locations()

def check_bomb(sub,bombs):
    global game_end
    global s
    for i in bombs:
        if sub.xcor() < i.xcor() + 19 and sub.xcor() > i.xcor() - 19 and sub.ycor() < i.ycor() + 19 and sub.ycor() > i.ycor() - 19:
            winsound.PlaySound("bomb_sound.wav", winsound.SND_ASYNC)
            s = 0.015
            i.hideturtle()
            sc.update()
            for i in range(1,5):
                sub.shape("blow"+f"{i}"+".gif")
                sc.update()
                time.sleep(0.2)
            
            time.sleep(0.5)    
            return True        
        
    return False

def moving():
    x = 0
    while 1:
        if x % 20 == 0:
            for i in bombs:
                i.goto(i.xcor(),i.ycor()-5)
            oxy.goto(oxy.xcor(),oxy.ycor()+5)
        elif x % 10 == 0:
            for i in bombs:
                i.goto(i.xcor(),i.ycor()+5)
            oxy.goto(oxy.xcor(),oxy.ycor()-5)
            
        if check_bomb(sub,bombs):
            winsound.PlaySound("8-bitcut.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
            start_button.shape("game_over.gif")
            start_button.showturtle()
            break
        check_oxy(sub,oxy)
        sub.forward(1.5)
        sc.update()
        time.sleep(s)
        x+= .5

        
            
        
        
def move_up():
    sub.setheading(90)
    winsound.PlaySound("start.wav", winsound.SND_ASYNC)
    sub.shape("up_submarine.gif")
    
def move_down():
    sub.setheading(270)
    winsound.PlaySound("start.wav", winsound.SND_ASYNC)
    sub.shape("down_submarine.gif")

def move_right():
    sub.setheading(0)
    winsound.PlaySound("start.wav", winsound.SND_ASYNC)
    sub.shape("right_submarine.gif")

def move_left():
    sub.setheading(180)
    winsound.PlaySound("start.wav", winsound.SND_ASYNC)
    sub.shape("left_submarine.gif")

def startclick(x,y):
    global scoring
    if x > -100 and x < 100 and y > -50 and y < 50:
        winsound.PlaySound("start.wav", winsound.SND_ASYNC)
        start_button.hideturtle()
        sc.update()
        for i in bombs:
            i.showturtle()
        new_locations()
        scoring = -1
        new_score()
        sub.shape("right_submarine.gif")
        move_right()
        moving()
        

        

turtle.listen()
turtle.onkey(key="w",fun=move_up)
turtle.onkey(key="s",fun=move_down)
turtle.onkey(key="d",fun=move_right)
turtle.onkey(key="a",fun=move_left)
turtle.onscreenclick(startclick)


while 1:
    start_button.goto(0,30)
    sc.update()
    time.sleep(.4)
    start_button.goto(0,20)
    sc.update()
    time.sleep(.4)
    
    
    
    

    
    

turtle.done()