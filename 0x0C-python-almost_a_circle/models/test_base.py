#!/usr/bin/python3
import unittest
import importlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import models.base
import models.rectangle
import models.square


class TestBase(unittest.TestCase):

    def setUp(self):
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_1NoArgs(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2TooManyArgs(self):
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertRaises(TypeError, Base, 23, 43)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_3None(self):
        a = Base(None)
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_4Id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        e = Base(14)
        self.assertEqual(e.id, 14)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_5NbObjs(self):
        c = Base()
        self.assertEqual(c.id, 1)

    # def test_to_json_string(self):
    #     ld = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
    #     self.assertEqual(
