import sqlite3
from scripts.Database.Database import Database

# inventory index range = 0-38. 0-29 is in inventory. 30-38 is in toolbar

class Inventory:
    def table(self):
        conn, c = Database().connect('inventory')

        c.execute("""CREATE TABLE inventory (
            item_type TEXT,
            slot_index INTEGER,
            char_id INTEGER
        )""")

        Database().close(conn)

    def load(self, char_id):
        conn, c = Database().connect('inventory')

        c.execute(f"""SELECT * FROM inventory WHERE char_id = {char_id}""")
        inventory_data_list = list()
        for inventory_data in c.fetchall():
            inventory_data_list.append(inventory_data)
            print(inventory_data)

        return inventory_data_list
        print(inventory_data_list)

        Database().close(conn)

    def place(self, item_type, slot_index, char_id):
        conn, c = Database().connect('inventory')

        if not self.check_index(slot_index, char_id):
            c.execute("""INSERT INTO inventory VALUES (:item_type, :slot_index, :char_id)""",
            {
                'item_type' : item_type,
                'slot_index' : slot_index, 
                'char_id' : char_id
            })
        else:
            self.replace(item_type, slot_index, char_id)
        
        Database().close(conn)
        
    
    def replace(self, item_type, slot_index, char_id):
        conn, c = Database().connect('inventory')

        c.execute("""UPDATE inventory SET
        item_type = :item_type

        WHERE slot_index = :slot_index AND char_id = :char_id""", 
        {
            'item_type' : item_type,
            'slot_index' : slot_index,
            'char_id' : char_id
        })

        Database().close(conn)

    def check_index(self, slot_index, char_id):
        conn, c = Database().connect('inventory')

        print(slot_index, char_id)
        c.execute(f"SELECT * FROM inventory WHERE slot_index = {slot_index} AND char_id = {char_id}")
        if c.fetchall():
            print(True)
            return True
        else:
            print(False)
            return False
        
        Database().close(conn)

    
if __name__ == "__main__":
    Inventory().table()