from cmu_graphics import *


def onStep():
    # Rotate the oar pole.
    # Place Your Code Here #

    # Reposition the oar fin to be centered on the end of the oar pole.
    # (HINT: You can set the centerX and centerY to be at the endpoint of
    #          the pole by using some of the pole's properties!)
    # Place Your Code Here #

    # Now rotate the oar fin to be angled in the correct direction.
    # (HINT: The pole and fin should rotate at the same speed)
    # Place Your Code Here #
    oarPole.rotateAngle += oarPole.rotateSpeed
    oarFin.rotateAngle += oarPole.rotateSpeed
    oarFin.centerX = oarPole.x1
    oarFin.centerY = oarPole.y1


def main():
    app.background = 'skyBlue'

    # This draws the kayak.
    Oval(200, 210, 350, 90, fill='magenta')
    Oval(200, 180, 400, 45, fill='skyBlue')


if __name__ == '__main__':
    main()
    # This creates the oar.
    oarPole = Line(200, 75, 200, 300, lineWidth=5)
    oarPole.rotateSpeed = 5

    oarFin = Oval(200, 50, 40, 80, fill='gold')

    # This draws the water.
    Rect(0, 230, 400, 170, fill='blue', opacity=85)
    cmu_graphics.run()
