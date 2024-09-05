from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.xmove = 10
        self.ymove = 10

    def move(self):
        self.penup()
        self.newx = self.xcor() + self.xmove
        self.newy = self.ycor() + self.ymove
        self.goto(self.newx, self.newy)

    def bounce(self):
        self.ymove *= -1

    def collide(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.collide()