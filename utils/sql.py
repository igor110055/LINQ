import os
import sqlite3
from datetime import datetime, timedelta

import pandas as pd

BASE_PATH = os.curdir


class SQLInterface:
    def __init__(self, db_str=os.path.join(BASE_PATH, "utils", "linq_db.db")) -> None:
        self.conn = sqlite3.connect(db_str)
        self.cur = self.conn.cursor()

    def new_table(self):
        self.conn.execute("CREATE TABLE test_table(tgID int, tbUsername varchar(255));")

    def insert_entry(self):
        self.conn.execute(
            "INSERT INTO test_table (tgID, tbUsername) VALUES (234, 'NathanBrowne');"
        )
        self.conn.commit()

    def available_tables(self):
        self.cur.execute('SELECT name from sqlite_master where type= "table"')
        return self.cur.fetchall()

    def get_result(self, table):
        return pd.read_sql_query("SELECT * FROM {};".format(table), self.conn)

    def df_to_table(self, df, name):
        df.to_sql(name=name, con=self.conn)


def main():
    sql = SQLInterface()

    print(sql.get_result("events"))


if __name__ == "__main__":
    main()
