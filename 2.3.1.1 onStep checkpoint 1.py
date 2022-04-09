from cmu_graphics import *


def onStep():
    # Rotate the spinning circle by 3 degrees every time onStep is run.
    # Place Your Code Here #
    spinningCircle.rotateAngle += 3


def main():
    app.background = 'grey'


if __name__ == '__main__':
    main()
    spinningCircle = Circle(200, 200, 200, fill=gradient('crimson', 'lavender', start='top'))
    cmu_graphics.run()
