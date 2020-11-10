# file for test cases for breadfactory.py

from breadfactory import BreadFactory
import unittest

class TestBreadFactory(unittest.TestCase):
    factory = BreadFactory()

    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertNotEqual(self.factory.make_dough('sugar', 'flour'), 'dough')

    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough('dough'), 'bread')
    
    def test_run_factory(self):
        self.assertTrue(self.factory.run_factory('water', 'flour'))