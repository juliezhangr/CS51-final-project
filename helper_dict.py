# helper_dict.py

# CS51 Final Project
# takes an array of tokens and creates a dictionary mapping 
# each token to the number of occurrences of that token

import os, sys

def create(tokenlist):
    tokencount = [tokenlist.count(p) for p in tokenlist]
    dictionary = dict(zip(tokenlist,tokencount))
    return dictionary
