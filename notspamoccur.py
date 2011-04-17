# notspamoccur.py
# CS51 Final Project - Preya, Ryaan, Jeff, Julie
# Spam filter - database module
# This module groups the functions that deal with the sqlite database of tokens and occurences.
# --to be used in training mode
# 

import sys
import sqlite


    # database loader: returns sqlite database object, either new or saved (unit -> sql object)
    def load ():
        try:
            connection = sqlite.connect('spamtable.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE notspamoccur (token STRING PRIMARY KEY, occurences FLOAT)')
        except sql_load_error as e:
            print ("error in loading")
            sys.exit(2) 

    # replace - when having same token, will replace the entry (string -> double -> unit)
    def update (token, o):
        t = "'" + token + "'"
        statement = token + ',' + 
        cursor.execute('REPLACE INTO notspamoccur (token, occurences) VALUES (' + statement + ')')
    
    # removes word entry from database (string -> unit)
    def remove (t):
        t = "'" + token + "'"
        cursor.execute('DELETE * FROM notspamoccur WHERE token = ' + t )

    # gets the spam probability given a token (string -> float)
    def getOccur (token):
        t = "'" + token + "'"
        cursor.execute('SELECT occurences FROM notspamoccur WHERE token =' + t)

