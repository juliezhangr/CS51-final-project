#!/usr/bin/python

# main.py
# this is the main script for 
# the program

import get_mail
import local_mail
import config
import get_mail

def main():
    config.init()
    get_mail.get_mail() 
    print "Welcome to Dragon Filter!"
    print "Filtering..."
    print "Done!"

if __name__ == '__main__':
    main()

