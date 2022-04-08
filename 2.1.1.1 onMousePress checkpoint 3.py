from cmu_graphics import *


def onMousePress(x, y):
    # Draw the circle that the X is drawn on top of. It should be drawn where the
    # mouse is pressed.
    # (HINT: Remember to press and hold the ctrl key to use the inspector!)
    # Place Your Code Here #
    Circle(x, y, 50, fill=gradient("lime", "black"))

    # Draw the 4-pointed star that makes the X shape. The inspector shows
    # that it has a roundness and a rotateAngle set!
    # (HINT: You can ignore or delete the "pass" below. It prevents an error
    #          that appears when you have no code indented inside onMousePress.)
    # Place Your Code Here #
    Star(x, y, 50, 4, fill=gradient("yellow", "lime"), roundness=20, rotateAngle=45)
    pass


def main():
    app.background = gradient('black', 'navy')

    cmu_graphics.run()


if __name__ == '__main__':
    main()
