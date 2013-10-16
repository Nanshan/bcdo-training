#!/usr/bin/python

import unittest

from calculation import *

class testCalculation(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add(2,2))

    def testSub(self):
        self.assertEqual(2, sub(4,2))

if __name__ == '__main__':
    unittest.main()
