#!/usr/bin/python
import sys
import argparse
from libcloudinit import conn,region

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
        parser.add_argument("-n", "--instance-count", help="Maximum instances to launch", default=1)
        parser.add_argument("-v", "--verbose", help="Verbose Output", action="store_true", default="False")
        parser.add_argument("-t", "--instance_type", help="Ec2 Instance Type", default="t1.micro")
        parser.add_argument("--role", help="roles defined in")
        parser.add_argument("-s", "--stack", help="")
        parser.add_argument("-b", "--branch", help="git branch")
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
           #image=conn.list_images(ex_image_ids=[ self.args.ami ])
           image=conn.list_images(ex_image_ids=[ ami ])[0]
           print image
           #print "Name: %s" % image.name
	   return 1
        except:
	   return 0
    
    def create_ec2_instance(self, args):
        arg_list=vars(self.args)
  	kwargs = { 'image': args.ami,
             	   'size': args.instance_type,
                  
		 }
        return conn.create_node(kwargs)

def main():
  ec2obj = ec2run()
  libobj = libcloudinit('EC2_US_WEST')
  args=ec2obj.parse_args(sys.argv[1:])
  ec2obj.print_args(args)
  print  libobj.region    
  ec2obj.create_ec2_instance(args)

if __name__ == '__main__':
    main()
