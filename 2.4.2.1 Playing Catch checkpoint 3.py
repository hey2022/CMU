from cmu_graphics import *


def onMousePress(x, y):
    # This moves the ball to 250 away from the mouse is pressed.
    ball.centerX = glove.centerX + 250
    ball.centerY = y

    # This resets the ball speed.
    ball.speedY = -25

    # This moves the stitching to the ball.
    ballStitches.centerX = ball.centerX
    ballStitches.centerY = ball.centerY


def onMouseMove(x, y):
    # This moves the glove to follow the mouse.
    gloveThumb.centerX = x + 60
    glove.centerX = x


def onStep():
    # Move the ball based on its speed custom properties. Then increase the
    # ball.speedY by 1.
    # Place Your Code Here #
    ball.centerX += ball.speedX
    ball.centerY += ball.speedY
    ball.speedY += 1

    # This moves the stitching to the ball.
    ballStitches.centerX = ball.centerX
    ballStitches.centerY = ball.centerY

    # Rotate the ball stitches counter-clockwise by 2.
    # Place Your Code Here #
    ballStitches.rotateAngle -= 2


def main():
    app.background = 'skyBlue'
    

if __name__ == '__main__':
    main()
    ball = Circle(350, 350, 50, fill='ghostWhite', border='black')
    ball.speedX = -5
    ball.speedY = -25

    ballStitches = Oval(350, 350, 50, 95, fill='ghostWhite', borderWidth=3, dashes=True,
                        border=gradient('red', 'red', 'red', 'ghostWhite'))

    gloveThumb = Oval(260, 375, 75, 120, fill='brown', border='black', rotateAngle=25)
    glove = Oval(200, 375, 130, 150, fill='brown', border='black')

    cmu_graphics.run()
