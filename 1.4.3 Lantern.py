from cmu_graphics import *


def main():
    app.background = gradient('lightSalmon', 'midnightBlue')

    # Draw the lantern's center.
    # (HINT: Use 3 Ovals centered at (200, 200) with borders!)
    # Place Your Code Here #
    Oval(200, 200, 180, 200, fill="red", borderWidth=8, border="darkred")
    Oval(200, 200, 120, 200, fill="orange", borderWidth=8, border="darkred")
    Oval(200, 200, 50, 200, fill="gold", borderWidth=8, border="darkred")

    # Draw the red strings that are below the lantern.
    # (HINT: You only need to draw a single Line!)
    # Place Your Code Here #
    Line(160, 350, 240, 350, lineWidth=100, dashes=True, fill="red")

    # This draws the rectangles at the top and bottom of the lantern.
    Rect(130, 260, 140, 40, fill='orangeRed', border='darkRed', borderWidth=8)
    Rect(130, 100, 140, 40, fill='orangeRed', border='darkRed', borderWidth=8)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
