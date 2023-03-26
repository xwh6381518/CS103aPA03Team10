'''

transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema
    (rowid,amount,category,date,desc)
    (rowid,amount,category,date,desc)
to Python Dictionaries as follows:

(7,1000,'2020-01-01','rent payment') <-->
{rowid:7,amount:1000, category: 'invoice',date:'2023-01-31',desc:'rent payment')

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

'''


import sqlite3


# Barry Wen
def to_dict(my_tu):
    ''' this method converts a tuple to a dictionary, 
    t is a tuple (rowid,amount,category,date,desc)'''
    print('t='+str(my_tu))
    tran = {'rowid': my_tu[0], 'amount': my_tu[1],
            'category': my_tu[2], 'date': my_tu[3], 'desc': my_tu[4]}
    return tran


class Transaction():
    '''The Transaction class'''

    # Barry Wen
    def __init__(self):
        self.run_query('''CREATE TABLE IF NOT EXISTS tran
                    (amount text, category text, date text, desc text)''', ())

    # Barry Wen
    def add(self, item):
        ''' create a transaction item and add it to the transaction table '''
        return self.run_query("INSERT INTO tran VALUES(?,?,?,?)",
                              (item['amount'], item['category'], item['date'], item['desc']))

    # Zhihan Li
    def delete(self, rowid):
        ''' delete a transaction item '''
        return self.run_query("DELETE FROM tran WHERE rowid=(?)", (rowid,))

    # Zhihan Li
    def select_category(self):
        ''' select all of the transactions by its category. '''
        return self.run_query("SELECT rowid, SUM(amount), category, date,"
                              + "desc FROM tran GROUP BY category", ())

    # Zhihan Li
    def select_day(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.run_query("SELECT rowid, SUM(amount), category,"
                              + "date, desc from tran GROUP BY date", ())

    # Zhihan Li
    def select_month(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.run_query("SELECT rowid, SUM(amount), category, SUBSTRING(date, 1, 7),"
                              + "desc from tran GROUP BY SUBSTRING(date, 1, 7)", ())

    # Wenhao Xie
    def select_year(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.run_query("SELECT rowid, SUM(amount), category, SUBSTRING(date, 1, 4),"
                              + "desc from tran GROUP BY SUBSTRING(date, 1, 4)", ())

    # Wenhao Xie
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM tran", ())

    # Wenhao Xie
    def run_query(self, query, tuple):
        ''' return all of the financial transactions as a list of dicts.'''
        con = sqlite3.connect('tracker.db')
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
