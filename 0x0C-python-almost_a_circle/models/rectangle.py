#!/usr/bin/python3
"""module for rectangle class"""

from models.base import Base


class Rectangle(Base):
    """class for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init a rectangle instance with specs"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attr"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """returns height attr"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attr"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """returns x attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x attr"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y attribute"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of a rectangle instance"""
        return self.width * self.height

    def display(self):
        """graphical representation of instance"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """user friendly print out of instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the attributes of a rectangle instance"""
        keys = ('id', 'width', 'height', 'x', 'y')
        if len(args) != 0:
            for k, v in zip(args, keys):
                setattr(self, v, k)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of object"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
