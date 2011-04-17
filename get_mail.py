# get_mail.py
# CS51 final project
# various email related functions
# which should be useful for testing




import imaplib
import sys
import getpass
import os
import config
# connect connects a user to his email client,
# and returns the connection object
def connect ():
	try: 
		m = imaplib.IMAP4_SSL(config.get_net("HOST"), int(config.get_net("PORT")))
		m.login(config.get_net("USER"), getpass.getpass())
		return m
	except imaplib.IMAP4.error as e:
		print (e.args[0])
		sys.exit(1)

# fetch_from_box takes an connection and a folder string, 
# and returns an array of tuples of message ids and messages
def _fetch_from_box (m, box, cmd):
    try:
        typ, mail_data = m.select(box)
        typ, msg_ids = m.search(None, cmd)
        mail_lst = []
        msg_ids = msg_ids[0].split(' ')
        for mid in msg_ids:
            if mid != '':
                typ, msg = m.fetch (mid, '(BODY.PEEK[])')
                mail_lst.append ((mid, msg[0])) 
        return mail_lst

    except imaplib.IMAP4.error as e:
        print (e.args[0])
        m.logout()
        sys.exit(1)
# fetch_all returns all mail from a 
# folder

def fetch_all (m, box):
    return _fetch_from_box (m, box, 'ALL')

# fetches_unread returns all unread mail 
# from a folder 
def fetch_unread (m, box):
    return _fetch_from_box (m, box, 'UNSEEN')

# write messages writes emails to
# a destination
# the names it uses are simple 1.txt 2.txt etc.
# since this is currently only for testing

def _write_msgs (msgs, dest):
    if not os.path.exists (dest):
        os.mkdir (dest)
    i = 0
    for msg in msgs:
        name = dest + str(i) + '.txt'
        f = open (name, "w")
        f.write(msg[1][1])
        f.close()
        i+=1

# get_mail is a function we can use 
# for testing, to get a lot of email into
# a local computer

def get_mail ():
    m = connect ()

    # downloads spam
    msgs = fetch_all (m, config.get_net("SPAM_SRC"))
    _write_msgs (msgs, config.get_net("SPAM_DEST"))

    msgs = fetch_all (m, config.get_net("INBOX_SRC"))
    _write_msgs (msgs, config.get_net("INBOX_DEST"))

    m.logout()

# write_msg_to_spam takes a connection, 
# a message id, and writes the message
# to the spam folder

# NOTE assumes connection
# is currently selecting the
# 'inbox' box, whatever that is

def write_msg_to_spam (m, mid):
    try:
        # copies the message
        m.copy (mid, config.get_net("SPAM_SRC"))
        m.store (mid, '+FLAGS', '\\Deleted')
    except imaplib.IMAP4.error as e:
        print e.args[0]
        m.logout()
        sys.exit(1)

