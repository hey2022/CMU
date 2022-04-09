from cmu_graphics import *


def onStep():
    # Rotate the Seconds hand.
    # (HINT: The Seconds hand is twice as long as it looks in the solution.
    #          It doesn't actually end at the center of the clock!)
    # Place Your Code Here #

    # Position the endpoints of the hideSecondsHand line to cover half of
    # the Seconds hand.
    # Place Your Code Here #
    secondsHand.rotateAngle += secondsHand.rotateSpeed
    hideSecondsHand.x2 = secondsHand.x2
    hideSecondsHand.y2 = secondsHand.y2


def main():
    app.background = 'aliceBlue'
    app.stepsPerSecond = 1

    Circle(200, 200, 200, fill='ghostWhite', border='darkGrey', borderWidth=10)
    Star(200, 200, 190, 60, roundness=25)
    Star(200, 200, 190, 12, roundness=15)
    Circle(200, 200, 175, fill='ghostWhite')


if __name__ == '__main__':
    main()
    secondsHand = Line(200, 35, 200, 365)
    secondsHand.rotateSpeed = 6

    hideSecondsHand = Line(200, 200, 200, 365, fill='ghostWhite', lineWidth=4)
    cmu_graphics.run()
