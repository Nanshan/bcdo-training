#!/usr/bin/python

import unittest
import sys
import run
import argparse
class testEc2Run(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testLength(self):
        self.assertEqual(len(run.dic_args),10)
    
    def testAmi(self):
        ec2run=run()
        self.assertEqual(ec2run.get_arg( ami), 'ami-123456')

if __name__ == '__main__':
    unittest.main()
