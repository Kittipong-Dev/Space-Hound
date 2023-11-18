import sqlite3

class Database:
    def connect(self, table_name):
        conn = sqlite3.connect(f'data/database/{table_name}.db')
        c = conn.cursor()
        return conn, c

    def close(self, conn):
        conn.commit()
        conn.close()