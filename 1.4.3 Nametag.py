from cmu_graphics import *


def main():
    app.background = gradient('silver', 'black', start='left-top')

    # Draws the name tag rope and card.
    Line(200, 95, 275, -15, fill='crimson', lineWidth=35)
    Rect(25, 75, 350, 275, fill=gradient('blue', 'limeGreen', 'yellow', 'orange', 'red', start='top'))
    Line(200, 95, 145, -15, fill='red', lineWidth=35)
    Oval(200, 95, 85, 15, fill='grey')

    # Draw the blank space on the name tag.
    # Place Your Code Here #
    Rect(50, 125, 300, 200, fill="white", borderWidth=4, border="black")

    # Draw all the text.
    # (HINT: The 'X' is drawn using a Label!)
    # Place Your Code Here #
    Label("Hello! My name is", 200, 175, fill="darkSlateBlue", font="arial", size=30, bold=True)
    Label("X", 75, 250, fill="black", font="arial", size=30)
    Label("Sam", 200, 240, fill="black", font="monospace", size=50)

    # Draw the line that indicates where to add the name.
    # Place Your Code Here #
    Line(100, 275, 330, 275)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
