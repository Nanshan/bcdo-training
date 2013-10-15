import getopt
import sys

options, remainder = getopt.getopt(sys.argv[1:], 'r:z:a:d:g:k:n:') 
for opt, arg in options:
    if opt in ('-r', 'region'):
        region=arg
        print 'region: ', region
    elif opt in ('-z', '--availability_zone'):
        zone=arg
        print 'availability_zone:   ', zone
    elif opt in ('-a', '--ami'):
        ami=arg
        print 'ami: ', ami
    elif opt in ('-f', '--user_data_file'):
        user_data_file=arg
        if  user_data_file is None:
           user_data_file= "None" 
        print 'user_data_file: ', user_data_file
    elif opt in ('-k', '--key'):
        key=arg       
        print 'key: ', key
    elif opt in ('-n', '--instance-count'):
        instance_count=arg
        print 'instance_count: ', instance_count
    elif opt in ('-d', ' --user-data'):
        user_data=arg
        print 'user_data: ', user_data
    elif opt in ('-t', '--instance_type'):
        instance_type=arg
        print 'instance_type: ', instance_type
    elif opt in ('-v', '--verbose'):
        verbose=False
        print 'verbose: ', verbose
    elif opt in ('-g', '--group'):
        group=arg
        print 'group: ', group
