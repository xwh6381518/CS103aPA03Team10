import pytest
import sqlite3
from transaction import to_dict, Transaction,tuples_to_dicts

# Zhihan Li
@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("100", "type1", "2020-01-01", "test1"), 
            ("200", "type2", "2020-01-01", "test2"),
            ("300", "type1", "2020-02-01", "test3"),
           ]

# Zhihan Li
@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

# Zhihan Li
@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])

# Zhihan Li
@pytest.fixture
def trans_path(tmp_path):
    yield tmp_path / 'trans.db'

# Zhihan Li
@pytest.fixture(autouse=True)
def trans(trans_path,tuples):
    "create and initialize the trans.db database in /tmp "
    con= sqlite3.connect(trans_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tran
                    (amount text, category text, date text, desc text)''')
    for i in range(len(tuples)):
        cur.execute('''insert into tran values(?,?,?,?)''',tuples[i])
    # create the todolist database
    con.commit()
    ts = Transaction(trans_path)
    yield ts
    cur.execute('''drop table tran''')
    con.commit()

# Zhihan Li
def test_select_all(trans, returned_dicts):
    ts = trans
    results = ts.select_all()
    expected = returned_dicts
    assert results == expected

# Zhihan Li
def test_select_day(trans, returned_dicts):
    ts = trans
    results = ts.select_day()
    list_ = []
    expected = []
    rid = 1
    for d in returned_dicts:
        sum = 0
        temp = {}
        if d['date'] not in list_:
            list_.append(d['date'])
            sum = int(d['amount'])
            temp['rowid'] = rid
            rid += 1
            temp['amount'] = sum
            temp['category'] = d['category']
            temp['date'] = d['date']
            temp['desc'] = d['desc']
            expected.append(temp) 
        else:
            for i in range(len(list_)):
                if expected[i]['date'] == d['date']:
                    sum = int(d['amount']) + int(expected[i]['amount'])
                    #returned_dicts[i]['amount'] = sum
                    expected[i]['amount'] = sum
                    rid += 1

    assert results == expected

# Zhihan Li
def test_select_category(trans, returned_dicts):
    ts = trans
    results = ts.select_category()
    list_ = []
    expected = []
    rid = 1
    for d in returned_dicts:
        sum = 0
        temp = {}
        if d['category'] not in list_:
            list_.append(d['category'])
            sum = int(d['amount'])
            temp['rowid'] = rid
            rid += 1
            temp['amount'] = sum
            temp['category'] = d['category']
            temp['date'] = d['date']
            temp['desc'] = d['desc']
            expected.append(temp) 
        else:
            for i in range(len(list_)):
                if expected[i]['category'] == d['category']:
                    sum = int(d['amount']) + int(expected[i]['amount'])
                    expected[i]['amount'] = sum
                    rid += 1
                    
    assert results == expected

# Zhihan Li
def test_delete(trans, returned_dicts):
    ts = trans
    ts.delete(1)
    results = ts.select_all()
    expected = returned_dicts
    assert results == expected[1:]


