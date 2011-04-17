# database.py
# CS51 Final Project - Preya, Ryaan, Jeff, Julie
# Spam filter - database module
# This module groups the functions that deal with the sqlite database of tokens and spamicities.
# 

import sys
import sqlite


    # database loader: returns sqlite database object, either new or saved (unit -> sql object)
    def load ():
        try:
            connection = sqlite.connect('spamtable.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE spamtable (token STRING PRIMARY KEY, spamprob FLOAT)')
            cursor.execute('CREATE TABLE emailcount (type STRING PRIMARY KEY, count DOUBLE DEFAULT 0)')
        except sql_load_error as e:
            print ("error in loading")
            sys.exit(2) 

    # emailcount
    # gets the count for a type of email
    def getCount (typ):
        t = "'" + typ + "'"
        cursor.execute('SELECT count FROM emailcount WHERE type =' + t )

    # email count
    # updates email corpus counts - inserts if entry does not exist yet, otherwise updates
    def updatecount (typ, num):
        t = "'" + typ + "'"
        c = getCount(typ) + num
        cursor.execute('REPLACE INTO emailcount (type, count) VALUES (' + t + ',' + c + ')' ) 


    # spamtable
    # replace - when having same token, will replace the entry, otherwise will insert entry
    def replace (token, v):
        t = "'" + token + "'"
        cursor.execute('REPLACE INTO spamtable (token, spamprob) VALUES (' + t + ',' + v + ')')
    
    # spamtable
    # removes word entry from database (string -> unit)
    def remove (t):
        t = "'" + token + "'"
        cursor.execute('DELETE * FROM spamtable WHERE token = ' + t)

    # spamtable
    # gets the spam probability given a token (string -> float)
    def getProb (token):
        t = "'" + token + "'"
        cursor.execute('SELECT spamprob FROM spamtable WHERE token =' + t)




    
