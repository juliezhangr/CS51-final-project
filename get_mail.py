#!/usr/bin/python

# get_mail.py
# CS51 final project
# Implements the get_mail function, which connects 
# to a user's inbox, scans an inbox folder and a spam 
# folderINBOX' and 'SPAM' by default, and sorts these 
# into two folders, ./inbox and ./spam by default. 
# This should be useful for testing


# change these for your own values
HOST='imap.gmail.com'
PORT=993
USER='jatwood123@gmail.com'
INBOX_SRC='Inbox'
SPAM_SRC='[Gmail]/Spam'
INBOX_DEST='./inbox'
SPAM_DEST='./spam'


import imaplib
import sys
import getpass
import os

# connect connects a user to his email client,
# and returns the connection object
def connect ():
	try: 
		m = imaplib.IMAP4_SSL(HOST, PORT)
		m.login(USER, getpass.getpass())
		return m
	except imaplib.IMAP4.error as e:
		print (e.args[0])
		sys.exit(1)

# fetch_from_box takes an connection and a folder string, 
# and returns an array of messages
def fetch_from_box (m, box, cmd):
	try:
		typ, mail_data = m.select(box)
		typ, msg_ids = m.search(None, cmd)
		mail_lst = []
		msg_ids = msg_ids[0].split(' ')
		for mid in msg_ids:
			if mid != '':
				typ, msg = m.fetch (mid, '(BODY.PEEK[])')
				mail_lst.append (msg[0]) 
		return mail_lst

	except imaplib.IMAP4.error as e:
		print (e.args[0])
		sys.exit(1)
# fetch_all returns all mail from a 
# folder

def fetch_all (m, box):
	return fetch_from_box (m, box, 'ALL')

# fetches_unread returns all unread mail 
# from a folder 
def fetch_unread (m, box):
	return fetch_from_box (m, box, 'UNSEEN')

# write messages writes emails to
# a destination
# the names it uses are simple 1.txt 2.txt etc.
# since this is currently only for testing

def write_msgs (msgs, dest):
	if not os.path.exists (dest):
		os.mkdir (dest)
	i = 0
	for msg in msgs:
		name = dest + '/' + str(i) + '.txt'
		f = open (name, "w")
		f.write(msg[1])
		f.close()
		i+=1



def get_mail ():
	m = connect ()

	# downloads spam
	msgs = fetch_unread (m, SPAM_SRC)
	write_msgs (msgs, SPAM_DEST)

	msgs = fetch_all (m, INBOX_SRC)
	write_msgs (msgs, INBOX_DEST)

	m.logout()

# uncomment for testing
# get_mail()
