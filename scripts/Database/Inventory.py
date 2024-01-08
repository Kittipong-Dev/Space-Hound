import sqlite3
from scripts.Database.Database import Database

# inventory index range = 0-38. 0-8 is in inventory. 9-38 is in toolbar

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

        print(self.count(inventory_data_list))

        Database().close(conn)

        return inventory_data_list

    def count(self, inventory_data_list: list):
        ls: list = list(map(lambda x: x[0], inventory_data_list))

        all_types: list = list(map(lambda x: x[0], set(inventory_data_list)))

        return_obj: object = {}
        for t in all_types:
            return_obj[t] = ls.count(t)

        return return_obj

    def place(self, item_type, slot_index, char_id):
        conn, c = Database().connect('inventory')

        if not self.slot_full(item_type, slot_index, char_id):
            c.execute("""INSERT INTO inventory VALUES (:item_type, :slot_index, :char_id)""",
            {
                'item_type' : item_type,
                'slot_index' : slot_index, 
                'char_id' : char_id
            })
        else:
            self.replace(item_type, slot_index, char_id) ########## replce need fix
        
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

    def slot_full(self, item_type, slot_index, char_id):
        conn, c = Database().connect('inventory')

        c.execute(f"SELECT * FROM inventory WHERE slot_index = {slot_index} AND char_id = {char_id}")
        return_value = False
        data: list = c.fetchall()
        if data:
            if not(item_type in data[0]):
                return_value = True
            
        
        Database().close(conn)

        return return_value

    
if __name__ == "__main__":
    Inventory().table()