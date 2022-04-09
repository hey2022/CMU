from cmu_graphics import *


def onStep():
    # Increase the number of points that the sun has.
    # Place Your Code Here #
    sun.points += 2


def main():
    app.background = 'black'


if __name__ == '__main__':
    main()
    sun = Star(200, 200, 175, 5, fill=gradient('orangeRed', 'gold'))
    cmu_graphics.run()
