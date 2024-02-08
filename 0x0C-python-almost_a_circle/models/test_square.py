#!/usr/bin/python3
import unittest
import io
import importlib
from contextlib import redirect_stdout
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import models.base
import models.rectangle
import models.square


class TestSquare(unittest.TestCase):

    def setUp(self):
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_fromRect(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_wrongNumArgs(self):
        with self.assertRaises(TypeError, msg="__init__() missing 1 required positional argument: 'size'"):
            Square()
        with self.assertRaises(TypeError, msg="__init__() takes from 2 to 5 positional arguments but 8 were given"):
            Square(2, 12, 23, 12, 34, 54, 23)

    def test_twoArgs(self):
        e = Square(14, 23)
        self.assertEqual(e.size, 14)
        self.assertEqual(e.x, 23)

    def test_keyWordArgs(self):
        c = Square(size=34, id=4, x=2)
        self.assertEqual(c.id, 4)
        self.assertEqual(c.size, 34)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 0)

    def test_type(self):
        li = [2, 4]
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, 'dsaf', 23)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, li, 23)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square('sdf', 23, 23)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(li, 23, 23)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 23, 'sdfds')
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, li)

    def test_value(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0, 2, 23)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(2, -1, 23)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(2, 3, -4)

    def test_area(self):
        c = Square(3)
        self.assertEqual(c.area(), 9)

    def test_display(self):
        a = Square(2, 1, 1)
        s = '\n ##\n ##\n'
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

        a = Square(2)
        s = '##\n##\n'
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

        a = Square(2, 1)
        s = ' ##\n ##\n'
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

    def test_update(self):
        c = Square(21, 32, 44, 21)
        c.update(5, 4, 3, 2)
        self.assertEqual(c.id, 5)
        self.assertEqual(c.size, 4)
        self.assertEqual(c.x, 3)
        self.assertEqual(c.y, 2)

        d = Square(21, 32, 44, 21)
        d.update(5, 4, 3, 2, 35, 32, 222, 343)
        self.assertEqual(d.id, 5)
        self.assertEqual(d.size, 4)
        self.assertEqual(d.x, 3)
        self.assertEqual(d.y, 2)

        e = Square(21, 32, 44, 21)
        e.update(5, 4, x=35)
        self.assertEqual(e.id, 5)
        self.assertEqual(e.size, 4)
        self.assertEqual(e.x, 32)
