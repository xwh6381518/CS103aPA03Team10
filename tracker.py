'''
tracker is an app that maintains a financial transactions list
just as with the transactions code in this folder.

it offers the user the following options and makes calls to the Transaction class to update the database.

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
    (rowid,amount,date,desc)
to Python Dictionaries as follows:

(7,'1000','2020-01-01','rent payment') <-->

{rowid:7,
 amount:'1000',
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


from transactions import Transaction
import sys


# Wenhao Xie
def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    translist = Transaction()
    if arglist == []:
        print_usage()
    elif arglist[0] == "show":
        print_trans(trans=translist.selectAll())
    elif arglist[0] == "quit":
        sys.exit()
    elif arglist[0] == 'add':
        if len(arglist) != 4:
            print_usage()
        else:
            transaction = {
                'amount': arglist[1], 'date': arglist[2], 'desc': arglist[3]}
            translist.add(transaction)
    elif arglist[0] == 'delete':
        if len(arglist) != 2:
            print_usage()
        else:
            translist.delete(arglist[1])
    elif arglist[0] == 'sum_day':
        print_trans(trans=translist.selectDay())
    elif arglist[0] == 'sum_month':
        print_trans(trans=translist.selectMonth())
    elif arglist[0] == 'sum_year':
        print_trans(trans=translist.selectYear())
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
                args = ['add', args[1], args[2], " ".join(args[3:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)


toplevel()
