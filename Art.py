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

# Begin pattern section


def pattern_1(turt):
    """
    A triangle pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(50, 100)
    for i in range(41):
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
    x = random.randint(25, 75)
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
    for y in range(10):
        for i in range(3):
            turt.forward(x)
            turt.left(120)
        turt.left(45)
        turt.forward(x)


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


def pattern_9(turt):
    """
    A plus-shaped pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 75)
    y = random.randint(10, 50)
    turt.begin_fill()
    for i in range(4):
        turt.forward(x)
        turt.left(90)
        turt.forward(x)
        turt.right(90)
        turt.forward(y)
        turt.right(90)
    turt.end_fill()


def pattern_10(turt):
    """
    A circular pattern made of triangles that can be randomly drawn.
    :param turt: The turtle object being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(5, 15)
    for y in range(75):
        for i in range(3):
            turt.forward(x)
            turt.left(120)
        turt.left(5)
        turt.forward(10)


def pattern_11(turt):
    """
    A circular pattern made up of smaller circles that can be randomly drawn.
    :param turt: The turtle object being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(10, 50)
    for i in range(75):
        turt.circle(x)
        turt.left(5)
        turt.forward(20)


def pattern_12(turt):
    """
    A spiral that is built out of squares that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 75)
    for y in range(25):
        for i in range(4):
            turt.forward(x)
            turt.right(90)
        turt.right(20)
        turt.forward(10)
        x = x + 5


def pattern_13(turt):
    """
    A pattern that is made up of hexagons that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 75)
    for y in range(6):
        for i in range(6):
            turt.forward(x)
            turt.right(60)
        turt.right(60)


def pattern_14(turt):
    """
    A spiraling pattern that stamps the turtle on the screen in each iteration that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(10, 25)
    for i in range(15):
        turt.stamp()
        turt.right(45)
        turt.forward(x)
        x = x + 5


def pattern_15(turt):
    """
    A circular pattern made up of pentagons that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 50)
    for y in range(75):
        for i in range(5):
            turt.forward(x)
            turt.left(72)
        turt.left(5)
        turt.forward(x)


def pattern_16(turt):
    """
    A square-based flower pattern that can be randomly drawn.
    :param turt: The turtle object that is being used to draw.
    :return:
    """
    turt.color((random.random(), random.random(), random.random()))
    x = random.randint(25, 75)
    for y in range(20):
        for i in range(4):
            turt.forward(x)
            turt.right(90)
        turt.right(20)


# End pattern section


def main():
    """
    The main function which draws a random shape, a random pattern, and then loops indefinitely.
    :return: None
    """
    turt = turtle.Turtle()
    turt.shape("turtle")
    wn = turtle.Screen()
    wn.bgcolor("white")
    turt.speed(0)
    turt.pensize(1.5)
    turt.forward(-120)
    turt.write("Enjoy your new art!", move=True, align="left", font=("Arial", 20, "normal"))
    x = True
    while x is True:
        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))  # Moves the turtle to a random location
        turt.pendown()

        draw_shapes(turt, random.randint(3, 6))  # Draws a random polygon

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))  # Moves the turtle to a random location
        turt.pendown()

        pattern_list = [pattern_1, pattern_2, pattern_3, pattern_4, pattern_5, pattern_6, pattern_7, pattern_8, pattern_9,
                        pattern_10, pattern_11, pattern_12, pattern_13, pattern_14, pattern_15, pattern_16]
        random.choice(pattern_list)(turt)  # Picks a random pattern from pattern_list and draws it.

        turt.penup()
        turt.goto(random.randint(-300, 300), random.randint(-300, 300))  # Moves the turtle to a random location
        turt.pendown()


main()
