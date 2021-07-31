from container import Canvas
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return " ({}, {}) ".format(self.x, self.y)


class Rectangle:
    """Rectangle creating a Rectangle Object

    When a Rectangle object is created some functions like get_polar can be used to retrieve polars.
    """
    def __init__(self, start: Point, end: Point):
        """
        :param start:
        :param end:
        """
        self.start = start
        self.end = end

    def get_polars(self):
        """ all the polar co-ordinates for the rectangle object

        :return: list of polars
        """
        width = self.end.x - self.start.x
        height = self.end.y - self.start.y

        return (width, 0), (height, 90), (width, 90), (height, 90)


    def __repr__(self):
        return "Rectangle with co-ordinates: [{}, {}]".format(self.start, self.end)


