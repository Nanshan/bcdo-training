#!/usr/bin/python

import unittest
import sys
from ec2run import ec2run
import argparse
class testEc2Run(unittest.TestCase):
    def setUp(self):
        self.ec2=ec2run()
    def tearDown(self):
        pass

    def testLength(self):
        self.args=self.ec2.parse_args( [] )
        self.args=vars(self.args)
        self.assertEqual(len(self.args),10)
    
    def testAmi(self):
        self.args=self.ec2.parse_args( ['-a', 'ami-123456'] )
        self.args=vars(self.args)
        self.assertEqual(self.ec2.get_arg('ami'), 'ami-123456')

if __name__ == '__main__':
    unittest.main()
