import turtle
import random

def draw_flower(t, size):
    t.color(random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple']))
    for _ in range(8):
        t.forward(size)
        t.backward(size)
        t.right(45)

def draw_flowers(num_flowers, flower_size):
    screen = turtle.Screen()
    screen.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-flower_size * num_flowers / 2, 0)
    t.pendown()

    for _ in range(num_flowers):
        draw_flower(t, flower_size)
        t.penup()
        t.forward(flower_size * 2)
        t.pendown()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    num_flowers = int(input("请输入要绘制的花朵数量："))
    flower_size = int(input("请输入每朵花的大小："))
    draw_flowers(num_flowers, flower_size)