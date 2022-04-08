from cmu_graphics import *


def main():
    app.background = 'deepSkyBlue'

    # Draw the tire!
    # (HINT: The Inspector displays information in the order of shapes that
    #          are drawn. If the first color the inspector shows is 'black', then
    #          the first shape has a fill of 'black'!)
    # Place Your Code Here #
    Circle(200, 200, 250, fill=gradient("black", "darkSlateGrey", "black", start="top"))
    Circle(200, 200, 175, fill=gradient("dimGrey", "white", start="left"))
    Circle(200, 200, 130, fill="black")
    Star(200, 200, 145, 10, fill="dimgrey", roundness=70)
    Star(200, 200, 175, 10, fill=gradient("dimGrey", "white", start="left"), roundness=40)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
