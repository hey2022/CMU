from cmu_graphics import *

import random


def draw_flake(x, y, r, edges, rotate, offset, smooth, range_start, range_end, depth):
    if depth > 0:
        Star(x, y, r, edges, rotateAngle=rotate, roundness=smooth,
             fill=rgb(random.randint(range_start, range_end), random.randint(range_start, range_end),
                      random.randint(range_start, range_end)))
        for i in range(edges):
            new_x, new_y = getPointInDir(x, y, i * 360 / edges + offset, r)
            draw_flake(new_x, new_y, r / 2, edges, rotate, offset, smooth, range_start, range_end, depth - 1)


def main():
    app.background = gradient(rgb(255, 0, 255), rgb(0, 255, 255))
    Oval(200, 200, 400, 200, fill=rgb(0, 0, 255), opacity=50)
    Oval(200, 200, 200, 400, fill=rgb(0, 0, 255), opacity=50)
    Circle(200, 200, 200, fill=rgb(153, 255, 204), opacity=50)
    Rect(5, 5, 90, 20, fill=rgb(153, 255, 204), border=rgb(0, 0, 0), borderWidth=2)
    Label("Cool Recursion", 50, 15, size=10, bold=True, italic=True, font="monospace")
    Line(10, 395, 390, 395, lineWidth=10, dashes=True, fill=rgb(153, 255, 204))
    app.setMaxShapeCount(2147483647)
    # draw_flake(x, y, r, edges, rotate, offset, smooth, range_start, range_end, depth)
    draw_flake(200, 200, 100, 6, 90, 0, 0, 0, 255, 5)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
