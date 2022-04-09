from cmu_graphics import *


def onStep():
    # Rotate the gears by changing their rotateAngle.
    # (HINT: Notice the direction each gear is rotating in!)
    # (HINT: The smallest gear rotates twice as fast as the larger ones.)
    # Place Your Code Here #
    bigGear.rotateAngle += 1
    mediumGear.rotateAngle -= 1
    smallGear.rotateAngle -= 2


def main():
    # This draws the machine.
    Rect(0, 0, 400, 400, fill='gray')
    Line(0, 200, 400, 200, lineWidth=40)
    Rect(100, 375, 200, 25)
    Rect(25, 25, 350, 350, fill='lightGrey')
    Circle(300, 50, 10, fill='crimson')
    Circle(330, 50, 10, fill='green')


if __name__ == '__main__':
    main()
    bigGear = Star(140, 140, 100, 30, fill='lightGrey', border='slateGray', borderWidth=25, roundness=90)
    mediumGear = Star(280, 245, 80, 30, fill='lightGrey', border='lightSlateGray', borderWidth=25, rotateAngle=20, roundness=90)
    smallGear = Star(137, 285, 50, 15, fill='lightGrey', border='lightSlateGrey', borderWidth=15, rotateAngle=15, roundness=80)
    # This draws the center of the gears
    Circle(140, 140, 20, fill='darkSlateGrey')
    Circle(280, 245, 10, fill='darkSlateGrey')
    Circle(137, 285, 5, fill='darkSlateGrey')
    cmu_graphics.run()
