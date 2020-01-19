import turtle
wn=turtle.Screen()
wn.title('pong')
wn.bgcolor('green')
wn.setup(width=800, height=600)
wn.tracer(0)
score_a=0
score_b=0
#paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('black')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0,0)
ball.dx=.52
ball.dy=-.52
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Thanos:0  Avengers :0',align='center',font=('Courier',24,'normal') )

line1=turtle.Turtle()
line1.speed(0)
line1.shape('square')
line1.shapesize(stretch_wid=50,stretch_len=.5)
line1.color('white')
line1.penup()
line1.goto(320,0)

line2=turtle.Turtle()
line2.speed(0)
line2.color('white')
line2.shapesize(stretch_wid=50,stretch_len=.5)
line2.shape('square')
line2.penup()
line2.goto(-320,0)

line3=turtle.Turtle()
line3.speed(0)
line3.color('blue')
line3.shapesize(stretch_wid=50,stretch_len=.65)
line3.shape('square')
line3.penup()
line3.goto(-20,0)

line4=turtle.Turtle()
line4.speed(0)
line4.color('white')
line4.shapesize(stretch_wid=.5,stretch_len=32)
line4.shape('square')
line4.penup()
line4.goto(0,0)


def paddle_a_up():
    y=paddle_a.ycor()
    if y< 275 :
        y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    if y > -275 :
        y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    if y< 275 :
        y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    if y > -275 :
        y-=20
    paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddle_a_up,'w')    
wn.onkeypress(paddle_a_down,'s')   
wn.onkeypress(paddle_b_up,'Up')    
wn.onkeypress(paddle_b_down,'Down')   

while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write('Thanos:{}  Avengers :{}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write('Thanos:{}  Avengers :{}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor() -40) :
        ball.setx(340)        
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor() -40) :
        ball.setx(-340)        
        ball.dx*=-1
        
                    
    if ball.xcor() <0:
        paddle_a.sety(ball.ycor()-30)
