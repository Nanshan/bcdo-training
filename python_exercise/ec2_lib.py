#!/usr/bin/python
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

class ec2run(object):
    def __inti__(self):
        pass 
      
    def parse_args(self, args):
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
        self.args=parser.parse_args(args)
        return self.args

    def get_arg(self, arg):
        return self.args.__getattribute__(arg)

    def print_args(self,args):
        arg_list=vars(args)
        for key in arg_list:
            print "%s: %s" % (key, self.get_arg(key))
 
    def validate_image(self, ami):
        try:       
#           image=conn.list_images(ex_image_ids=[ self.args.ami ])
            image=conn.list_images(ex_image_ids=[ ami ])[0]
            print image 
            #print "Name: %s" % image.name

            return 1 
        except:
            return 0

    def validate_zone(self, zone): 
        zone=conn.list_zon

def main():
   ec2obj = ec2run()
   args=ec2obj.parse_args(sys.argv[1:])
#   print args
  # ec2obj.print_args(args)
   print ec2obj.validate_image('ami-3a36027f')

if __name__ == '__main__':
    main()
>>>>>>> 3cbc965372529a8d6affcc51d1e0ef66216748ab
