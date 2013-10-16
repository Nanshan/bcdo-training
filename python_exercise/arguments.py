#!/usr/bin/python

import sys

def parse_args(argv=None):
    if argv is None:
       argv = [ ]
    return argv[1:]

def main(argv=None):
    print "Here is the main method"
    print parse_args(argv)

if __name__ == '__main__':
    main(sys.argv)
