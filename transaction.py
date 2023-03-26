'''

transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema
    (rowid,amount,category,date,desc)
to Python Dictionaries as follows:

(7,1000,'2020-01-01','rent payment') <-->
{rowid:7,amount:1000, category: 'invoice',date:'2023-01-31',desc:'rent payment')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

'''


import sqlite3
import os


# Barry Wen
# this method converts a tuple to a dictionary
def toDict(t):
    ''' t is a tuple (rowid,amount,category,date,desc)'''
    print('t='+str(t))
    tran = {'rowid': t[0], 'amount': t[1], 'category': t[2], 'date': t[3], 'desc': t[4]}
    return tran


'''the Transaction class'''


class Transaction():
    # Barry Wen
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS tran
                    (amount text, category text, date text, desc text)''', ())

    # Barry Wen
    def add(self, item):
        ''' create a transaction item and add it to the transaction table '''
        return self.runQuery("INSERT INTO tran VALUES(?,?,?,?)", (item['amount'], item['category'], item['date'], item['desc']))

    # Zhihan Li
    def delete(self, rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM tran WHERE rowid=(?)", (rowid,))
    
    # Zhihan Li
    def selectCategory(self):
        ''' select all of the transactions by its category. '''
        return self.runQuery("SELECT rowid, SUM(amount), category, date, desc FROM tran GROUP BY category", ())

    # Zhihan Li
    def selectDay(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid, SUM(amount), category, date, desc from tran GROUP BY date", ())

    # Zhihan Li
    def selectMonth(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid, SUM(amount), category, SUBSTRING(date, 1, 7), desc from tran GROUP BY SUBSTRING(date, 1, 7)", ())

    # Wenhao Xie
    def selectYear(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid, SUM(amount), category, SUBSTRING(date, 1, 4), desc from tran GROUP BY SUBSTRING(date, 1, 4)", ())

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
