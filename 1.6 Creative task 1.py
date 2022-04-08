from cmu_graphics import *

import random


def main():
    app.background = gradient(rgb(255, 0, 255), rgb(0, 255, 255))
    Oval(200, 200, 400, 200, fill=rgb(0, 0, 255), opacity=50)
    Oval(200, 200, 200, 400, fill=rgb(0, 0, 255), opacity=50)
    Circle(200, 200, 200, fill=rgb(153, 255, 204), opacity=50)
    Rect(5, 5, 90, 20, fill=rgb(153, 255, 204), border=rgb(0, 0, 0), borderWidth=2)
    Label("Cool Recursion", 50, 15, size=10, bold=True, italic=True, font="monospace")
    Line(10, 395, 390, 395, lineWidth=10, dashes=True, fill=rgb(153, 255, 204))
    Star(200, 200, 100, 6, rotateAngle=90,
         fill=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), roundness=25)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
