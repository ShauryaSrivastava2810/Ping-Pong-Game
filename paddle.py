from turtle import Turtle

class Paddle:
    def __init__(self, x, y):
        self.t = Turtle(shape="square")
        self.t.color("white")
        self.t.shapesize(stretch_wid=5, stretch_len=1)
        self.t.penup()
        self.t.setx(x)
        self.t.sety(y)

    def go_up(self):
        self.new_y = self.t.ycor() + 20
        self.t.goto(self.t.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.t.ycor() - 20
        self.t.goto(self.t.xcor(), self.new_y)