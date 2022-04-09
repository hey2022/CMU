from cmu_graphics import *


def onMouseMove(x, y):
    # Move the glove and its thumb around to follow the mouse. Notice that the solution
    # only moves the glove's x position, not its y position.
    # (HINT: To position the glove's thumb, look at how far away from the glove
    #          we drew the thumb!)
    # Place Your Code Here #
    gloveThumb.centerX = x + 60
    glove.centerX = x


def main():
    app.background = 'skyBlue'


if __name__ == '__main__':
    main()
    gloveThumb = Oval(260, 375, 75, 120, fill='brown', border='black', rotateAngle=25)
    glove = Oval(200, 375, 130, 150, fill='brown', border='black')
    cmu_graphics.run()
