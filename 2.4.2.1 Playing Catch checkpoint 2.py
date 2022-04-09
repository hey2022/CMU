from cmu_graphics import *


def onMousePress(x, y):
    # This moves the ball to be 250 away from the mouse in the x-position.
    ball.centerX = glove.centerX + 250
    ball.centerY = y

    # Move the ball stitches to where the ball is.  # Place Your Code Here #
    ballStitches.centerX = glove.centerX + 250
    ballStitches.centerY = y


def onMouseMove(x, y):
    # This moves the glove.
    gloveThumb.centerX = x + 60
    glove.centerX = x


def main():
    app.background = 'skyBlue'


if __name__ == '__main__':
    main()
    # Name this circle ball, and give it two custom properties: speedX and speedY.
    # speedX should be -5 and speedY should be -25.
    # Fix Your Code Here #
    ball = Circle(350, 350, 50, fill='ghostWhite', border='black')
    ball.speedX = -5
    ball.speedY = -25

    ballStitches = Oval(350, 350, 50, 95, fill='ghostWhite', borderWidth=3, dashes=True,
                        border=gradient('red', 'red', 'red', 'ghostWhite'))

    gloveThumb = Oval(260, 375, 75, 120, fill='brown', border='black', rotateAngle=25)
    glove = Oval(200, 375, 130, 150, fill='brown', border='black')
    cmu_graphics.run()
