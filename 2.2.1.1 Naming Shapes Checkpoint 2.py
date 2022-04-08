from cmu_graphics import *


def onMousePress(x, y):
    # Move tabby to the x position of the mouse.
    # Place Your Code Here #
    tabby.centerX = x

    # This moves tabby 200 above where the mouse was pressed.
    tabby.centerY = y - 200


def main():
    Rect(0, 0, 400, 200, fill='lightGrey')
    Rect(0, 200, 400, 200, fill='thistle')


if __name__ == '__main__':
    main()
    # Name this rectangle tabby.
    # Place Your Code Here #
    tabby = Rect(200, 200, 50, 50, fill='darkOrange')

    cmu_graphics.run()
