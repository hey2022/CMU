from cmu_graphics import *


def onMousePress(x, y):
    # Draw a star using the x as the rotateAngle.
    # Place Your Code Here #
    Star(200, 200, 200, 5, fill="white", opacity=20, rotateAngle=x)
    pass


def main():
    app.background = 'black'

    cmu_graphics.run()


if __name__ == '__main__':
    main()
