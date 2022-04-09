from cmu_graphics import *


def onStep():
    # Move greenCircle to the right and orangeCircle up.
    # (HINT: We have created two custom properties for you above.)
    # (HINT: Notice that orangeCircle.speedY on line 7 is negative!)
    # Place Your Code Here #
    greenCircle.centerX += greenCircle.speedX
    orangeCircle.centerY += orangeCircle.speedY


def main():
    app.background = 'aliceBlue'
    

if __name__ == '__main__':
    main()
    greenCircle = Circle(0, 200, 30, fill='seaGreen')
    greenCircle.speedX = 1

    orangeCircle = Circle(200, 400, 30, fill='darkOrange')
    orangeCircle.speedY = -2
    cmu_graphics.run()
