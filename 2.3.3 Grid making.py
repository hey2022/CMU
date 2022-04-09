from cmu_graphics import *


def onStep():
    # Change the grey and blue lines every step to get the animation that is in
    # the solution.
    # Place Your Code Here #
    greyLine.lineWidth += 1
    blueLine.lineWidth += 1


def main():
    Line(15, 0, 15, 400, fill='silver', lineWidth=30)
    Line(385, 0, 385, 400, fill='silver', lineWidth=30)
    Line(0, 15, 400, 15, fill='silver', lineWidth=30)
    Line(0, 385, 400, 385, fill='silver', lineWidth=30)


if __name__ == '__main__':
    greyLine = Line(0, 200, 400, 200, fill='lightGrey', dashes=True)
    blueLine = Line(200, 0, 200, 400, fill='steelBlue', dashes=True, opacity=50)
    main()
    cmu_graphics.run()
