from cmu_graphics import *


def main():
    # Draw both WALL-E and Eve.
    # (HINT: Don't be overwhelmed by how much there is here! Just pick one
    #          part to draw first and focus on that. When you finish that part,
    #          pick another one, and another, and so on.)
    # Place Your Code Here #
    app.background = "black"

    # Eve
    Oval(210, 225, 30, 120, fill="gainsboro", rotateAngle=10)
    Oval(370, 225, 30, 120, fill="gainsboro", rotateAngle=-10)
    Line(230, 170, 210, 285, fill="black", lineWidth=10)
    Line(350, 170, 370, 285, fill="black", lineWidth=10)
    Oval(290, 200, 130, 250, fill=gradient("silver", "white", "silver", start="left"))
    Oval(290, 105, 190, 175, fill="black")
    Oval(290, 125, 130, 120, fill=gradient("silver", "white", "silver", start="left"))
    Oval(290, 175, 125, 50, fill=gradient("silver", "white", start="top"))
    Oval(290, 145, 120, 50, fill=gradient("silver", "white", "silver", start="left"))
    Oval(290, 120, 110, 70, fill="black")
    Oval(265, 120, 35, 25, fill="deepSkyBlue", rotateAngle=15)
    Oval(315, 120, 35, 25, fill="deepSkyBlue", rotateAngle=-15)
    Oval(265, 130, 50, 10, fill="black", rotateAngle=15)
    Oval(315, 130, 50, 10, fill="black", rotateAngle=-15)

    # Wall-E
    Circle(45, 210, 10, fill="darkOrange")
    Circle(175, 210, 10, fill="darkOrange")
    Line(20, 170, 40, 205, fill="orange", lineWidth=15)
    Line(190, 165, 180, 205, fill="orange", lineWidth=15)
    Line(0, 135, 20, 170, fill="silver", lineWidth=10)
    Line(200, 120, 190, 165, fill="silver", lineWidth=10)
    Oval(200, 120, 25, 25, fill="silver")
    Line(185, 115, 200, 120, fill="black", lineWidth=6)
    Rect(5, 265, 40, 75, fill=gradient("dimGrey", "darkGrey", "dimGrey", start="top-left"))
    Rect(175, 265, 40, 75, fill=gradient("dimGrey", "darkGrey", "dimGrey", start="top-left"))
    Rect(45, 170, 175 - 45, 200 - 170, fill=gradient("orange", "darkOrange", start="left"))
    Rect(45, 200, 175 - 45, 315 - 200, fill="darkOrange")
    Line(50, 220, 170, 220, lineWidth=35, fill="gainsboro")
    Line(90, 220, 130, 220, lineWidth=35, fill="silver")
    Line(60, 265, 160, 265, fill="orangeRed", lineWidth=30, dashes=True)
    Circle(160, 300, 10, fill="red")
    Label("WALL- ", 125, 300, fill="black", font="arial", size=15, bold=True)
    Label("E", 160, 300, fill="white", font="arial", size=15, bold=True)
    Rect(45, 200, 175 - 45, 315 - 200, fill=gradient("khaki", "sienna"), opacity=40)
    Oval(95, 145, 30, 35, fill="black", borderWidth=3, border="dimGrey")
    Oval(125, 145, 30, 35, fill="black", borderWidth=3, border="dimGrey")
    Line(110, 145, 110, 165, fill="lightGrey", lineWidth=10)
    Line(110, 165, 110, 190, fill=gradient("darkOrange", "sienna", start="left"), lineWidth=15)
    Oval(90, 140, 45, 35, fill="aliceBlue", border="silver", borderWidth=3, rotateAngle=-25)
    Oval(130, 140, 45, 35, fill="aliceBlue", border="silver", borderWidth=3, rotateAngle=25)
    Circle(90, 140, 10, fill=gradient("dodgerBlue", "darkBlue"))
    Circle(130, 140, 10, fill=gradient("dodgerBlue", "darkBlue"))

    cmu_graphics.run()


if __name__ == '__main__':
    main()
