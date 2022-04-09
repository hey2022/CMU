from cmu_graphics import *


def onMousePress(x, y):
    # This moves the ball to be at the top of the canvas, and have the same
    # x-position as the mouse.
    ball.centerX = x
    ball.centerY = 0


# Change this to use onStep instead of onMouseMove.
# Fix Your Code Here #
def onStep():
    # This moves the ball down by 10.
    ball.centerY = ball.centerY + 10


def main():
    app.background = 'dodgerBlue'


if __name__ == '__main__':
    main()
    ball = Circle(200, 0, 40, fill=gradient('red', 'darkRed', start='left-top'))
    cmu_graphics.run()
