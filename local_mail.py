# local_mail.py
# CS51 final project
# functions to read in a series of emails
# as well as sort them.

# change these for your values for testing

SPAM_SRC='./spam_src/'
INBOX_SRC='./inbox_src/'
INBOX_DEST='./inbox/'
SPAM_DEST='./spam/'


import os
# read mail opens all files in the inbox or 
# spam src, and returns an array of tuples of file names and message strings
def _read_mail (directory):
    names = os.listdir(directory)
    mail = []
    for f in names:
        fp = open (directory + f, "r")
        print directory + f
        mail.append((f, fp.read()))
        fp.close()
    return mail

def read_spam ():
    return _read_mail(SPAM_SRC)

def read_inbox():
    return _read_mail(INBOX_SRC)

# sort takes a tuple of a file name and a message, 
# and sends it to spam

def sort (msg):
    dest = SPAM_DEST
    if not os.path.exists (dest):
        os.mkdir (dest)
    f = open (dest + msg[0], "w")
    f.write (msg[1])
    f.close()
    os.remove(INBOX_SRC + msg[0])


