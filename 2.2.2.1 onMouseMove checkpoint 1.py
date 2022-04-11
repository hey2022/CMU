from cmu_graphics import *


def onMouseMove(x, y):
    # Rotate the star using either the x or the y. We have named the
    # star "spinningStar" for you.
    # (HINT: Remember that all shapes have a rotateAngle property!)
    # Place Your Code Here #
    spinningStar.rotateAngle = x
    pass


def main():
    app.background = 'aliceBlue'
    Line(200, 200, 200, 400, fill=gradient('cyan', 'darkBlue'), lineWidth=20)


if __name__ == '__main__':
    main()
    spinningStar = Star(200, 200, 150, 3, fill=gradient('pink', 'orangeRed'))
    cmu_graphics.run()
