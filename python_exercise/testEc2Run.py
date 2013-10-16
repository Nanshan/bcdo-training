#!/usr/bin/python

import unittest
import ec2run 
import sys
import argparse
class testEc2Run(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testLength(self):
        self.assertEqual(len(ec2run.dic_args),10)
    
    def testAmi(self):
        self.assertEqual(ec2run.dic_args['ami'], 'ami-123456')

if __name__ == '__main__':
    unittest.main()
