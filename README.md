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