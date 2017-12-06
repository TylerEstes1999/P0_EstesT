######################################################################################
# Author: Tyler Estes
# Username: EstesT
#
# Assignment: P0: Final Project
# Purpose: My final project for CSC 226. This class will be used to draw random shapes
#          and patterns on a turtle window indefinitely.
# ####################################################################################

# A test suite for this file was not needed, since there are no fruitful functions in the program.

import turtle
import random


def draw_shapes(turt, side_num):
    """
    Draws randomly colored shapes using the turtle library
    :param side_num: The number of sides of the shape
    :param turt: A turtle object to draw with.
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))
    angle = 360 / side_num
    y = random.randint(25, 100)
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
    x = random.randint(25, 100)
    for i in range(x):
        turt.forward(x)
        turt.right(123)


def pattern_2(turt):
    """
    A star pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    turt.begin_fill()
    x = random.randint(25, 100)
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
    x = random.randint(25, 100)
    for y in range(10):
        for i in range(4):
            turt.forward(x)
            turt.left(90)
        turt.left(45)
        turt.forward(30)


def pattern_4(turt):
    """
    A spiraling triangle pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 100)
    for i in range(21):
        x = x + 5
        turt.forward(x)
        turt.left(120)


def pattern_5(turt):
    """
    A pattern made up of circles that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 100)
    for i in range(8):
        turt.circle(x)
        turt.left(60)


def pattern_6(turt):
    """
    A shuriken-shaped pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 100)
    turt.begin_fill()
    for y in range(10):
        for i in range(3):
            turt.forward(x)
            turt.left(120)
        turt.left(45)
        turt.forward(x)
    turt.end_fill()


def pattern_7(turt):
    """
    A pattern made of pentagons that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 100)
    for y in range(20):
        turt.forward(x)
        turt.right(18)
        for i in range(5):
            turt.forward(x)
            turt.right(72)


def pattern_8(turt):
    """
    A spiraling square pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 100)
    for i in range(36):
        x = x + 5
        turt.forward(x)
        turt.right(90)

def main():
    """
    The main function which draws a random shapes, a random pattern, and then loops indefinitely.
    :return: None
    """
    turt = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("white")
    turt.speed(0)
    turt.pensize(1)
    x = True
    while x is True:
        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

        draw_shapes(turt, random.randint(3, 6))

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

        pattern_list = [pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6, pattern_7, pattern_8]
        random.choice(pattern_list)(turt)

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))
        turt.pendown()

main()
