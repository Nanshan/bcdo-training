#!/usr/bin/env python

import os
import re
import sys
import argparse
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.EC2_US_WEST)

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', None)
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', None)
assert AWS_ACCESS_KEY is not None
assert AWS_SECRET_KEY is not None
conn = Driver(AWS_ACCESS_KEY, AWS_SECRET_KEY)

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--region", help="ec2 region")

parser.add_argument("-z", "--availability_zone", help="ec2 availability zone")
parser.add_argument("-a", "--ami", help="AMI name")
parser.add_argument("-d", "--user-data", help="User data string")
parser.add_argument("-f", "--user_data_file", help="Read user data from file")
parser.add_argument("-g", "--group", help="Ec2 security group name/id")
parser.add_argument("-k", "--key", help="Ec2 Keypair name")
parser.add_argument("-n", "--instance-count", help="Maximum instances to launch")
parser.add_argument("-v", "--verbose", help="Verbose Output", action="store_true", default="False")
parser.add_argument("-t", "--instance_type", help="Ec2 Instance Type", default="t1.micro")
args = parser.parse_args()

dic_args=vars(args)

for key in dic_args.keys():
    print "%s: %s" % (key, dic_args[key])
def get_arg(self,arg):
    return eval('self.args.%s' % arg)

