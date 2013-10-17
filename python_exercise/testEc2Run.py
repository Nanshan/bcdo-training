#!/usr/bin/python

import unittest
import sys
from ec2_lib import ec2run
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
    
    def test_get_ami(self):
        self.args=self.ec2.parse_args( ['-a', 'ami-123456'] )
        self.args=vars(self.args)
        self.assertEqual(self.ec2.get_arg('ami'), 'ami-123456')

    def test_NOT_ValidateAmi(self):
        self.assertEqual(self.ec2.validate_image('ami-123456'),0)  

    def test_ValidateAmi(self):
        self.assertEqual(self.ec2.validate_image('ami-3a36027f'),1)

if __name__ == '__main__':
    unittest.main()
