from cmu_graphics import *


def onMousePress(x, y):
    # Change the circle to be drawn 200 above where the mouse is pressed.
    # (HINT: You'll need to adjust the centerY of this Circle.)
    # Fix Your Code Here #
    Circle(x, y - 200, 20, fill='slateBlue')


def main():
    Rect(0, 0, 400, 200, fill='lightSalmon')
    Rect(0, 200, 400, 200, fill='darkTurquoise')

    cmu_graphics.run()


if __name__ == '__main__':
    main()
