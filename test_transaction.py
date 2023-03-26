import pytest
import sqlite3
from transaction import toDict, Transaction

#Zhihan Li
@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("100", "type1", "2020-01-01", "test1"), 
            ("200", "type2", "2020-01-02", "test2"),
            ("300", "type1", "2020-02-01", "test3")
           ]

