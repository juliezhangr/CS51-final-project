#!/usr/bin/env python

# main.py
# this is the main script for 
# the program

import get_mail
import local_mail
import config
import sys
import getopt
import re

def main():
    config.init()
    new
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'gfteio')
# executes program, based on options, executes training or filtering
        args_hash = {}
        for opt in opts:
            args_hash[opt[0]] = _split_args(opt[1])
            # TODO, handle arguments, assert no clashes
        print "Filtering..."
        print "Done!"
    except getopt.GetoptError as e:
        print e.args[0]

if __name__ == '__main__':
    main()

def _split_args (s):
    return s.split(';')

