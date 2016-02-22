from pyglet_helper.objects import Sphere
from pyglet_helper.util import Rgb, Vector


class Ellipsoid(Sphere):
    """
    An Ellipsoid object
    """
    def __init__(self, height=1.0, width=1.0, length=1.0, color=Rgb(), pos=Vector(0, 0, 0)):
        """

        :param width: The ellipsoid's width.
        :type width: float
        :param height: The ellipsoid's height.
        :type height: float
        :param length: The ellipsoid's length.
        :type length: float
        :param color: The object's color.
        :type color: pyglet_helper.util.Rgb
        :param pos: The object's position.
        :type pos: pyglet_helper.util.Vector
        """
        super(Ellipsoid, self).__init__(color=color, pos=pos)
        self._height = None
        self._width = None
        self.height = height
        self.width = width
        self.length = length

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if h < 0:
            raise ValueError("height cannot be negative")
        self._height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        if w < 0:
            raise ValueError("width cannot be negative")
        self._width = w

    @property
    def size(self):
        return Vector(self.axis.mag(), self.height, self.width)

    @size.setter
    def size(self, s):
        if s.x < 0:
            raise ValueError("length cannot be negative")
        if s.y < 0:
            raise ValueError("height cannot be negative")
        if s.z < 0:
            raise ValueError("width cannot be negative")
        self.axis = self.axis.norm() * s.x
        self.height = s.y
        self.width = s.z

    @property
    def scale(self):
        return Vector(self.axis.mag(), self.height, self.width) * 0.5

    def degenerate(self):
        return not self.visible or self.height == 0.0 or self.width == 0.0 or self.axis.mag() == 0.0