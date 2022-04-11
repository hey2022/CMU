from cmu_graphics import *


def onMouseMove(x, y):
    # Move dot1 to follow the mouse.
    # Place Your Code Here #
    dot1.centerX = x
    dot1.centerY = y

    # Move dot2 to be a mirrored version of dot1.
    # (HINT: The distance from dot2 to the right edge of the canvas is x!)
    # Place Your Code Here #
    dot2.centerX = 400 - x
    dot2.centerY = y


def main():
    app.background = gradient('dodgerBlue', 'navy')

    Line(200, 400, 200, 0, dashes=True)


if __name__ == '__main__':
    main()
    dot1 = Circle(100, 100, 20, fill=gradient('lightCoral', 'crimson'))
    dot2 = Circle(300, 100, 20, fill=gradient('paleGreen', 'seaGreen'))
    cmu_graphics.run()
    