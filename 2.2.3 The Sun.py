from cmu_graphics import *


def onMouseMove(x, y):
    # Change the oval's width and height to be 25 more than mouseX and mouseY.
    # Fix Your Code Here #
    Oval(200, 200, x + 25,  y + 25, fill=None, border='orangeRed', borderWidth=1, opacity=20)
    
    
def main():
    app.background = 'black'


if __name__ == '__main__':
    main()
    cmu_graphics.run()
