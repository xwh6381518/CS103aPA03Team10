import pytest
import sqlite3
from transaction import to_dict, Transaction,tuples_to_dicts

# Zhihan Li
@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("100", "type1", "2020-01-01", "test1"), 
            ("200", "type2", "2020-01-02", "test2"),
            ("300", "type1", "2020-02-01", "test3")
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

