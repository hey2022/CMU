from cmu_graphics import *


def main():
    app.background = 'black'

    # Draw the perfume in the bottle.
    # Place Your Code Here #
    Oval(165, 290, 240, 220, fill="plum")

    # This draws the straw and spray nozzle.
    Rect(155, 130, 20, 60, fill='silver')
    Circle(105, 105, 55, fill='pink')
    Circle(165, 115, 20, fill='grey')
    Circle(180, 115, 3, fill='silver')

    # Draw the bottle glass.
    # Place Your Code Here #
    Star(165, 280, 130, 29, opacity=50, fill=gradient("white", "silver", "white", start="left"), roundness=97)

    # This draws the bottle outline.
    Star(165, 280, 130, 29, fill=None, border='white', borderWidth=15, roundness=97)

    # Draw the perfume spray.
    # Place Your Code Here #
    Star(275, 115, 100, 2000, fill="plum", roundness=20)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
