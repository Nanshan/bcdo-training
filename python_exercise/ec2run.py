#!/usr/bin/python
import sys
import argparse
<<<<<<< HEAD
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



=======
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


def main():
  ec2obj = ec2run()
  args=ec2obj.parse_args(sys.argv[1:])
  ec2obj.print_args(args)

if __name__ == '__main__':
    main()
>>>>>>> 3cbc965372529a8d6affcc51d1e0ef66216748ab
