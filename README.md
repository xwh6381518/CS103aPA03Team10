# CS103aPA03Team10
### Team member: Barry Wen, Wenhao Xie, Zhihan Li
### This is Team 10's Program Assignment 3. In this assignment, we write 3 files and using 1 database.
* transaction.py
* tracker.py
* test_transaction.py
* tracker.db
### By running the tracker.py, we could connected to the tracker.db database, and we could interact with database by this list of commands:
* quit
* show transactions
* add transaction
* delete transaction
* summarize transactions by date
* summarize transactions by month
* summarize transactions by year
* summarize transactions by category
* print this menu

## Pylint:
### The following are pylint test results, we received all above 9
xiewenhao@xiewenhaodeMacBook-Air CS103aPA03Team10 % pylint tracker.py
************* Module tracker
tracker.py:82:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:87:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:91:0: R0912: Too many branches (14/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.45/10 (previous run: 9.45/10, +0.00)

xiewenhao@xiewenhaodeMacBook-Air CS103aPA03Team10 % pylint transaction.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.09/10, +0.91)

xiewenhao@xiewenhaodeMacBook-Air CS103aPA03Team10 % pylint test_transaction.py
************* Module test_transaction
test_transaction.py:46:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)

------------------------------------------------------------------
Your code has been rated at 9.89/10 (previous run: 9.89/10, +0.00)

## Pytest: 
### we have passed all test cases in test_transaction.py, here is the result.
pytest -v
============================================================================= test session starts =============================================================================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0 -- C:\Users\zhiha\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\zhiha\Desktop\testProject\CS103aPATeam10
plugins: anyio-3.6.2
collected 7 items

test_transaction.py::test_select_all PASSED                                                                                                                              [ 14%]
test_transaction.py::test_select_day PASSED                                                                                                                              [ 28%]
test_transaction.py::test_select_category PASSED                                                                                                                         [ 42%]
test_transaction.py::test_delete PASSED                                                                                                                                  [ 57%]
test_transaction.py::test_add PASSED                                                                                                                                     [ 71%]
test_transaction.py::test_select_month PASSED                                                                                                                            [ 85%]
test_transaction.py::test_select_year PASSED                                                                                                                             [100%]

============================================================================== 7 passed in 0.25s ==============================================================================

## Tracker.py:
## Tracker.py makes calls to the Transaction class to update the database.

## Transaction.oy:
## transaction.py stores financial transactions with five fields: item #, amount, category, date and description
## It allows the user to read and update the database as need.