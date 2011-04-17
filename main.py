#!/usr/bin/env python

# main.py
# this is the main script for 
# the program

import get_mail
import local_mail
import config
import sys
import getopt

def main():
    config.init()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'g')
        for opt in opts:
            if opt[0] == '-g':
                get_mail.get_mail()
        print "Filtering..."
        print "Done!"
    except getopt.GetoptError as e:
        print e.args[0]

if __name__ == '__main__':
    main()

