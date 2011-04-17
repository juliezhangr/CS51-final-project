# config.py
# This module has functions for initializing 
# two hash tables, _local, and _net, which
# contain configuration instructions
# for the script. These are private, and
# are instead accessed via the get_attr("") 
# function

_config = './.spamconfig'
_local = {}
_net = {}

import re
import sys
def init():
    localmatch = re.compile("LOCALMAIL")
    netmatch = re.compile("NET")
    globalmatch = re.compile("OTHER")
    matcher = re.compile("[A-Z_]+=\S+")
    splitter = re.compile("=")
    comments = re.compile("#")
    local = False
    net = False
    other = False
    fp = open (_config, "r")
    for l in fp:
        l = l.rstrip()
        if comments.match(l) == None:
            if not localmatch.match(l) == None:
                local = True
                net = False
                other = False
            elif not netmatch.match(l) == None:
                local = True
                net = False
                other = False
            elif not globalmatch.match(l)==None:
                other = True
                net = False
                local = False
            elif not matcher.match(l) == None :
                l = splitter.split(l)
                if local:
                    _local[l[0]] = l[1]
                elif net:
                    _net[l[0]] = l[1]

def get_local (s):
    try:
        return _local[s]
    except KeyError:
        print ("No such attribute")
        sys.exit(1)

def get_net (s):
    try:
        return _local[s]
    except KeyError:
        print ("No such attribute")
        sys.exit(1)

def get_other(s):
    try:
        return _other[s]
    with KeyError:
        print ("No such attribute")
        sys.exit(1)

def set_local(k, v);
    _local[k] = v

def set_net(k, v):
    _net[k] = v

def set_other(k,v):
    _other[k] = v
