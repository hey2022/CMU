from cmu_graphics import *


def onMousePress(x, y):
    # Use the Inspector to help you draw each part of the sushi roll.
    # (HINT Each sushi is drawn with only 5 shapes.)

    # Draw the sushi body with an Oval, a Rect, and another Oval.
    # (HINT: The first Oval is drawn at x, y, the Rect is 20 pixels
    #          to the left of that, and the second Oval is drawn 20 pixels
    #          below the first Oval.
    # Place Your Code Here #
    Oval(x, y, 40, 20, fill="black")
    Rect(x - 20, y, 40, 20, fill=gradient("black", "dimGrey", start="left"))
    Oval(x, y + 20, 40, 20, fill=gradient("black", "dimGrey", start="left"))

    # Draw the rice with an Oval.
    # Place Your Code Here #
    Oval(x, y, 38, 18, fill="white")

    # Draw the salmon using a Rect.
    # (HINT: The Rect is drawn at x - 5, y - 5.)
    # Place Your Code Here #
    Rect(x - 5, y - 5, 10, 10, fill=gradient("salmon", "crimson", start="top"))

    pass


def main():
    app.background = 'floralWhite'

    # bamboo plates
    Rect(20, 250, 360, 100, fill=gradient('peru', 'burlyWood', start='left'))
    Line(20, 300, 380, 300, fill='floralWhite', lineWidth=100, dashes=(1, 10))
    Rect(10, 240, 20, 120, fill='peru')
    Rect(370, 240, 20, 120, fill='peru')

    Rect(20, 50, 360, 100, fill=gradient('peru', 'burlyWood', start='left'))
    Line(20, 100, 380, 100, fill='floralWhite', lineWidth=100, dashes=(1, 10))
    Rect(10, 40, 20, 120, fill='peru')
    Rect(370, 40, 20, 120, fill='peru')

    # wasabi
    Circle(40, 75, 15, fill='yellowGreen')
    Circle(40, 275, 15, fill='yellowGreen')

    # ginger
    Circle(40, 115, 15, fill='pink')
    Circle(40, 315, 15, fill='pink')

    # soy sauce bowl
    Rect(70, 170, 60, 60, fill='maroon')
    Rect(71, 171, 58, 58, fill=gradient('gainsboro', 'white', start='left'))
    Line(72, 172, 128, 228, fill='gainsboro')
    Line(128, 172, 72, 228, fill='gainsboro')

    # soy sauce
    Rect(85, 185, 30, 30, fill=gradient('black', 'maroon'))

    # chopstick stand
    Rect(220, 180, 20, 40, fill=gradient('lightGray', 'white', start='left'))

    # Chopstick
    Line(200, 195, 350, 195, fill='peru', lineWidth=5)
    Line(200, 205, 350, 205, fill='peru', lineWidth=5)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
