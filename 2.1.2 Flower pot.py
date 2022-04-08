from cmu_graphics import *


def onMousePress(x, y):
    # Draw a flower where you click the mouse and connect its stem to the vase!
    # (HINT: Remember to use ctrl to see the inspector!)
    # Place Your Code Here #
    Line(200, 300, x, y, fill="limeGreen", lineWidth=5)
    Star(x, y, 20, 11, fill=gradient("yellow", "deepPink"))
    pass


def main():
    app.background = gradient('ghostWhite', 'powderBlue')

    # This draws the vase.
    Oval(200, 300, 50, 10, fill='limeGreen')
    Oval(200, 370, 100, 135, fill=gradient('dimGray', 'lightGrey', start='bottom'))
    Rect(175, 300, 50, 10, fill='silver')

    cmu_graphics.run()


if __name__ == '__main__':
    main()
