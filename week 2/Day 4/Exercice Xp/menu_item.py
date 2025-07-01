from db import connect_db

class MenuItem:
    def __init__(self, name, price):
        self.item_name = name
        self.item_price = price

    def save(self):
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Menu_Items (item_name, item_price)
                    VALUES (%s, %s)
                """, (self.item_name, self.item_price))
            conn.commit()
    
    def delete(self):
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM Menu_Items
                    WHERE item_name = %s
                """, (self.item_name,))
            conn.commit()

    def update(self, new_name, new_price):
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE Menu_Items
                    SET item_name = %s, item_price = %s
                    WHERE item_name = %s
                """, (new_name, new_price, self.item_name))
                self.item_name = new_name
                self.item_price = new_price
            conn.commit()

    def show(self):
        print(f"Item: {self.item_name}, Price: {self.item_price}")



