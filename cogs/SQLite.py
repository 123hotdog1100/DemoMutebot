import sqlite3
import os

DIR = os.path.dirname(__file__)
db = sqlite3.connect(os.path.join(DIR, "WarnsDB.db"))
SQL = db.cursor()


def create_table():
    SQL.execute('create table if not exists Warns("ID" integer not null primary key unique,"Username" text not null,  '
                '"Amount" integer)')


def data_lookup():
    SQL.execute('select Username from Warns where Username ="123hotdog1100"')
    is_there = SQL.fetchone()
    print(is_there[0])


def data_entry(ID: int, Username: str, Amount: int):
    SQL.execute("insert into Warns(ID, Username, Amount) values(?,?,?)", (ID, Username, Amount))
    db.commit()


def read_using_id(ID):
    SQL.execute(f"SELECT * FROM Warns WHERE ID={ID}")
    for row in SQL.fetchall():
        print(row[2])
        return row[2]


def update(ID):
    SQL.execute("SELECT * FROM Warns")
    current = read_using_id(ID)
    if current is None:
        pass
    elif current is not None:
        current = current + 1
    print(current)
    SQL.execute(f"UPDATE Warns SET Amount = {current} WHERE ID = {ID}")
    db.commit()

def clear(ID):
    SQL.execute(f"UPDATE Warns SET Amount = 0 WHERE ID = {ID}")
    db.commit()

def close():
    SQL.close()
    db.close()