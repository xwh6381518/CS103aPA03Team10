'''

transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema
    (rowid,amount,date,desc)
to Python Dictionaries as follows:

(7,1000,'2020-01-01','rent payment') <-->
{rowid:7,amount:1000,  category:'type of transaction, bill, invoice, etc.', date:'2023-01-31',desc:'rent payment')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

'''


import sqlite3
import os

# this method converts a tuple to a dictionary
#WZL
def toDict(t):
    ''' t is a tuple (rowid,amount,category,date,description)'''
    print('t='+str(t))
    tran = {'rowid': t[0], 'amount': t[1], 'category': t[2],
            'date': t[3], 'desc': t[4]}
    return tran


'''the Transaction class'''


class Transaction():
    #WZL
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS tran
                    (amount text, date text, desc text, category text)''', ())
        
    #Zhihan Li
    def delete(self, rowid):
        ''' delete the transaction of given rowid from databse. '''
        return self.runQuery("DELETE FROM tran WHERE rowid=(?)", (rowid))

    #Zhihan Li
    def selectDay(self, date):
        ''' return all of the transactions of selected day as a list of dicts.'''
        return self.runQuery("SELECT * from tran WHERE date=(?)", (date))
    
    #Zhihan Li
    def selectMonth(self, date):
        ''' return all of the transactions of selected month as a list of dicts.'''
        return self.runQuery("SELECT rowid, amount, SUBSTRING(date, 1, 7), desc, category from tran WHERE date=(?)", (date))
    
    #Zhihan Li
    def selectCategory(self, category):
        ''' return all of the transactions of selected category as a list of dicts.'''
        return self.runQuery("SELECT * from tran WHERE category=(?)", (category))

    # Wenhao Xie
    def selectYear(self, date):
        ''' return all of the transactions of selected year as a list of dicts.'''
        return self.runQuery("SELECT rowid, amount, SUBSTRING(date, 1, 4), desc, category from tran WHERE date=(?)", (date))

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
