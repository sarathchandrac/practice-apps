import turtle


class Canvas(object):
    def __init__(self, x=0, y=0):
        turtle.penup()
        turtle.goto(x, y)
        self.canvas = turtle.Turtle()

    def close(self):
        turtle.done()

    def draw_polars(self, polars: tuple) -> None:
        turtle.pendown()
        for polar in polars:
            print("draw distance{}, angle{}".format(polar[0], polar[1]))
            self.draw( distance=polar[0], angle=polar[1])

        turtle.penup()
        turtle.done()

    def draw(self, distance: float, angle: float) -> None:
        self.canvas.left(angle=angle)
        self.canvas.forward(distance=distance)
