'''
tracker is an app that maintains a financial transactions list
just as with the transactions code in this folder.

it offers the user the following options and makes calls to 
the Transaction class to update the database.

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Transaction, will map SQL rows with the schema
    (rowid,amount,category,date,desc)
to Python Dictionaries as follows:

(7,'1000','2020-01-01','rent payment') <-->

{rowid:7,
 amount:'1000',
 category:'invoice'
 date: '2020-01-01'
 desc:'rent payment',
 }

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''


# here are some helper functions ...

import sys
from transaction import Transaction


# Barry Wen
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            transaction quit
            transaction show
            transaction add amount category date description
            transaction delete item_id
            transaction sum_day
            transaction sum_month
            transaction sum_year 
            '''
          )


# Zhihan Li
def print_trans(trans):
    ''' print the transaction items '''
    if len(trans) == 0:
        print('no transaction to print')
        return
    print('\n')
    print("%-10s %-10s %-20s %-30s %-30s" %
          ('item #', 'amount', 'category', 'date', 'desc'))
    print('-'*80)
    for item in trans:
        values = tuple(item.values())  # (rowid,amount,category,date,desc)
        print("%-10s %-10s %-20s %-30s %-30s" % values)

# Wenhao Xie


def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    translist = Transaction()
    if arglist == []:
        print_usage()
    elif arglist[0] == "show":
        print_trans(trans=translist.select_all())
    elif arglist[0] == "quit":
        sys.exit()
    elif arglist[0] == 'add':
        if len(arglist) != 5:
            print_usage()
        else:
            transaction = {
                'amount': arglist[1], 'category': arglist[2],
                'date': arglist[3], 'desc': arglist[4]}
            translist.add(transaction)
    elif arglist[0] == 'delete':
        if len(arglist) != 2:
            print_usage()
        else:
            translist.delete(arglist[1])
    elif arglist[0] == 'sum_day':
        print_trans(trans=translist.select_day())
    elif arglist[0] == 'sum_month':
        print_trans(trans=translist.select_month())
    elif arglist[0] == 'sum_year':
        print_trans(trans=translist.select_year())
    elif arglist[0] == 'sum_category':
        print_trans(trans=translist.select_category())
    else:
        print(arglist, "is not implemented")
        print_usage()

# Wenhao Xie


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            if args[0] == 'add':
                # join everyting after the name as a string
                args = ['add', args[1], args[2], args[3], " ".join(args[4:])]
            process_args(args)
            print('-'*80+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*80+'\n'*3)


toplevel()
