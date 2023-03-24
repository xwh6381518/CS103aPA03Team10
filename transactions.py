'''

transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema
    (rowid,amount,date,desc)
to Python Dictionaries as follows:

(7,1000,'2020-01-01','rent payment') <-->
{rowid:7,amount:1000,date:'2023-01-31',desc:'rent payment')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

'''


import sqlite3
import os


'''the Transaction class'''


class Transaction():
    # Wenhao Xie
    def selectYear(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid, SUM(amount), SUBSTRING(date, 1, 4), desc from tran GROUP BY SUBSTRING(date, 1, 4)", ())

    # Wenhao Xie
    def selectAll(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM tran", ())

    # Wenhao Xie
    def runQuery(self, query, tuple):
        ''' return all of the financial transactions as a list of dicts.'''
        con = sqlite3.connect('tracker.db')
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
