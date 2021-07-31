import folium
import turtle
from container import Canvas
from geometry import Rectangle, Point


def test_rectangle():
    cnv = Canvas(0, 0)
    r1 = Rectangle(start=Point(1, 1), end=Point(100, 100))
    polars = r1.get_polars()
    cnv.draw_polars(polars=polars)
    cnv.close()


test_rectangle()

