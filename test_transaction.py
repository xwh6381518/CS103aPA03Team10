"pytest for tracker.py and transaction.py"
import sqlite3
import pytest
from transaction import to_dict, Transaction, tuples_to_dicts


# Wenhao Xie
@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("100", "type1", "2020-01-01", "test1"),
            ("200", "type2", "2020-01-02", "test2"),
            ("300", "type1", "2020-02-01", "test3")
            ]


# Wenhao Xie
@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]


# Wenhao Xie
@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])


# Zhihan Li
@pytest.fixture
def trans_path(tmp_path):
    "create a database path for pytest"
    yield tmp_path / 'trans.db'


# Zhihan Li
@pytest.fixture(autouse=True)
def trans(trans_path, tuples):
    "create and initialize the trans.db database in /tmp "
    con = sqlite3.connect(trans_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tran
                    (amount text, category text, date text, desc text)''')
    for i in range(len(tuples)):
        cur.execute('''insert into tran values(?,?,?,?)''', tuples[i])
    # create the todolist database
    con.commit()
    t_s = Transaction(trans_path)
    yield t_s
    cur.execute('''drop table tran''')
    con.commit()


# Zhihan Li
def test_select_all(trans, returned_dicts):
    "test for select_all method"
    t_s = trans
    results = t_s.select_all()
    expected = returned_dicts
    assert results == expected


# Zhihan Li
def test_select_day(trans, returned_dicts):
    "test for select_day"
    t_s = trans
    results = t_s.select_day()
    list_ = []
    expected = []
    rid = 1
    for r_d in returned_dicts:
        sum_val = 0
        temp = {}
        if r_d['date'] not in list_:
            list_.append(r_d['date'])
            sum_val = int(r_d['amount'])
            temp['rowid'] = rid
            rid += 1
            temp['amount'] = sum_val
            temp['category'] = r_d['category']
            temp['date'] = r_d['date']
            temp['desc'] = r_d['desc']
            expected.append(temp)
        else:
            for i in range(len(list_)):
                if expected[i]['date'] == r_d['date']:
                    sum_val = int(r_d['amount']) + int(expected[i]['amount'])
                    # returned_dicts[i]['amount'] = sum
                    expected[i]['amount'] = sum
                    rid += 1

    assert results == expected


# Zhihan Li
def test_select_category(trans):
    "test for select_category"
    t_s = trans
    results = t_s.select_category()
    expected = [{'rowid': 1, 'amount': 400, 'category': 'type1',
                 'date': '2020-01-01', 'desc': 'test1'},
                {'rowid': 2, 'amount': 200, 'category': 'type2',
                    'date': '2020-01-02', 'desc': 'test2'}]
    assert results == expected


# Zhihan Li
def test_delete(trans, returned_dicts):
    "test for delete"
    t_s = trans
    t_s.delete(1)
    results = t_s.select_all()
    expected = returned_dicts
    assert results == expected[1:]


# Barry Wen
def test_add(trans, returned_dicts):
    "test for add"
    t_s = trans
    new_transaction_tuple = ("400", "type3", "2020-03-01", "test4")
    new_transaction_dict = to_dict(
        (len(returned_dicts) + 1,) + new_transaction_tuple)

    trans.add(new_transaction_dict)
    results = t_s.select_all()
    expected = returned_dicts + [new_transaction_dict]
    assert results == expected


# Barry Wen
def test_select_month(trans, returned_dicts):
    "test for select_month"
    t_s = trans
    new_transaction_tuple = ("500", "type4", "2020-04-01", "test5")
    new_transaction_dict = to_dict(
        (len(returned_dicts) + 1,) + new_transaction_tuple)
    t_s.add(new_transaction_dict)
    expected = [
        {'rowid': 1, 'amount': 300, 'category': 'type1',
            'date': '2020-01', 'desc': 'test1'},
        {'rowid': 3, 'amount': 300, 'category': 'type1',
            'date': '2020-02', 'desc': 'test3'},
        {'rowid': 4, 'amount': 500, 'category': 'type4',
            'date': '2020-04', 'desc': 'test5'}
    ]
    results = t_s.select_month()
    assert results == expected


# Barry Wen
def test_select_year(trans, returned_dicts):
    "test for select_year"
    t_s = trans
    new_transaction_tuple = ("600", "type5", "2021-01-01", "test6")
    new_transaction_dict = to_dict(
        (len(returned_dicts) + 1,) + new_transaction_tuple)
    t_s.add(new_transaction_dict)
    results = t_s.select_year()
    expected = [
        {'rowid': 1, 'amount': 600, 'category': 'type1',
            'date': '2020', 'desc': 'test1'},
        {'rowid': 4, 'amount': 600, 'category': 'type5',
            'date': '2021', 'desc': 'test6'}
    ]
    assert results == expected
