# 用 turtle 画一个正方形：前进 100 像素，右转 90 度，重复 4 次
import turtle
turtle.pensize(12)
turtle.pencolor("purple")
turtle.speed(1)     

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()       