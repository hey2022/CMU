from cmu_graphics import *


def onMousePress(x, y):
    # Rotate the rectangle named rotatingSquare by adding to its .rotateAngle
    # property.
    # (HINT: Use the Inspector, click the mouse, and see how much the
    #          rotateAngle changed by!)
    # Place Your Code Here #
    rotatingSquare.rotateAngle += 15
    pass


def main():
    # This draws the background.
    Rect(0, 0, 400, 100, fill='lime')
    Rect(0, 100, 100, 200, fill=gradient('dodgerBlue', 'lime', start='top'))
    Rect(300, 100, 100, 200, fill=gradient('dodgerBlue', 'lime', start='top'))
    Rect(0, 300, 400, 100, fill='dodgerBlue')


if __name__ == '__main__':
    main()
    rotatingSquare = Rect(100, 100, 200, 200, fill=gradient('dodgerBlue', 'lime', start='right'))
    cmu_graphics.run()
