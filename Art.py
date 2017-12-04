######################################################################
# Author: Tyler Estes
# Username: EstesT
#
# Assignment: P0: Final Project
# Purpose: My final project for CSC 226. This class will be used to draw random shapes
#          and patterns on a turtle window indefinitely.
# ####################################################################
import turtle
import random


def draw_shapes(turt, side_num):
    """
    Draws randomly colored shapes using the turtle library
    :param side_num: The number of sides of the shape
    :param turt: A turtle object to draw with.
    :return: None
    """
    x = True
    turt.color((random.random(), random.random(), random.random()))
    angle = 360 / side_num
    y = random.randint(10, 50)
    while x is True:
        turt.begin_fill()
        for x in range(side_num):
            turt.forward(y)
            turt.right(angle)
        turt.end_fill()


def pattern_1(turt):
    """
    A triangle pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 150)
    for i in range(x):
        turt.forward(x)
        turt.right(123)


def pattern_2(turt):
    """
    A star pattern that can be randomly drawn
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    turt.begin_fill()
    x = random.randint(50, 150)
    for i in range(5):
        turt.forward(x)
        turt.left(144)
    turt.end_fill()


def pattern_3(turt):
    """
    A pattern made up of squares that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 75)
    for y in range(10):
        for i in range(4):
            turt.forward(x)
            turt.left(90)
        turt.left(45)
        turt.forward(30)


def pattern_4(turt):
    pass


def pattern_5(turt):
    pass


def main():
    """
    The main function which draws a random shapes, a random pattern, and then loops indefinitely.
    :return: None
    """
    turt = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("white")
    turt.speed(5)
    turt.pensize(1)
    x = True
    while x is True:
        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

        draw_shapes(turt, random.randint(3, 10))

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

        random.random(pattern_1(turt), pattern_2(turt), pattern_3(turt), pattern_4(turt), pattern_5(turt))

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

main()
