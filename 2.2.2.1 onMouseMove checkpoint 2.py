from cmu_graphics import *


def onMousePress(x, y):
    # Move the ball to the top of the canvas, above the mouse.
    # Place Your Code Here #
    ball.centerX = x
    ball.centerY = 0
    pass


def onMouseMove(x, y):
    # Move the ball down by 20.
    # Place Your Code Here #
    ball.centerY += 20
    pass


def main():
    app.background = 'dodgerBlue'


if __name__ == '__main__':
    main()
    ball = Circle(200, 0, 40, fill=gradient('red', 'darkRed', start='left-top'))
    cmu_graphics.run()
