from cmu_graphics import *


def onMousePress(x, y):
    # This draws the center of the pillow.
    Circle(x, y, 33, fill='lightCyan')

    # This draws the top half of the pillow.
    Star(x - 25, y - 25, 30, 3, fill='bisque', rotateAngle=-45)
    Star(x + 25, y - 25, 30, 3, fill='bisque', rotateAngle=45)

    # Draw the bottom half of the pillow.
    # Place Your Code Here #
    Star(x - 25, y + 25, 30, 3, fill='bisque', rotateAngle=-15)
    Star(x + 25, y + 25, 30, 3, fill='bisque', rotateAngle=15)


def main():
    app.background = 'lightGrey'

    Rect(10, 20, 380, 360, fill='saddleBrown')

    # This draws the mattress.
    Rect(30, 225, 340, 175, fill='ghostWhite')
    Line(55, 230, 0, 410, fill='ghostWhite', lineWidth=55)
    Line(345, 230, 400, 410, fill='ghostWhite', lineWidth=55)

    # This draws the blanket.
    Rect(0, 295, 400, 165, fill='steelBlue')
    Rect(0, 295, 400, 25, fill='lightBlue')

    cmu_graphics.run()


if __name__ == '__main__':
    main()
