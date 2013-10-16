#!/usr/bin/python

import unittest

from arguments import *

class testArguments(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNone(self):
        argv = None
        self.assertEqual(len(parse_args(argv)), 0)

    def testZero(self):
        argv=[] 
        self.assertEqual(len(parse_args(argv)), 0)  
    
    def testNumberOfArgs(self):  
        argv = [ 'testArguments.py', '-a', 'args_a']
        self.assertEqual(len(parse_args(argv)), len(argv)-1)

if __name__ == '__main__':
    unittest.main()
