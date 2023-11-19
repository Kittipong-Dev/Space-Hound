import sqlite3
from scripts.Database.Database import Database
class Character:

    INDEXPAIR = {
    'name' : 0,
    'level': 1,
    'exp': 2,
    'max_exp' : 3,
    'state': 4,
    }

    def table(self):
        conn, c = Database().connect('character')

        c.execute("""CREATE TABLE character (
            name TEXT,
            level INTEGER,
            exp REAL,
            max_exp REAL,
            state INTEGER
        )""")

        Database().close(conn)

    def create(self, name):
        conn, c = Database().connect('character')

        if len(self.query()) < 3:
            c.execute("""INSERT INTO character VALUES (:name, :level, :exp, :max_exp, :state)""",
            {
                'name' : name,
                'level' : 0,
                'exp' : 0,
                'max_exp' : 100,
                'state' : 1
            })
        else:
            print('char max')

        Database().close(conn)

    def save(self, char_id, level, exp, max_exp):
        conn, c = Database().connect('character')

        c.execute("""UPDATE character SET
            level = :level,
            exp = :exp,
            max_exp = :max_exp,
            state = :state


            WHERE oid = :oid""",
            {
                'level': level,
                'exp' : exp,
                'max_exp' : max_exp,
                'state' : 1,
                'oid' : char_id
            })

        Database().close(conn)

    def load(self, char_id):
        conn, c = Database().connect('character')

        c.execute(f"SELECT * FROM character WHERE oid = {char_id}")
        for char_data in c.fetchall():
            return char_data

        Database().close(conn)

    def delete(self, char_id):
        conn, c = Database().connect('character')

        c.execute("""UPDATE character SET
            state = :state


            WHERE oid = :oid""",
            {
                'state' : 0,
                'oid' : char_id
            })

        Database().close(conn)

    def query(self):
        conn, c = Database().connect('character')

        c.execute("SELECT *, oid FROM character WHERE state = 1")
        chars_id = list()
        for character in c.fetchall():
            chars_id.append(character[-1])
        
        return chars_id

        Database().close(conn)

if __name__ == '__main__':
    Character().table()