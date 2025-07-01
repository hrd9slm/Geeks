from db import connect_db

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM Menu_Items
                    WHERE item_name = %s
                """, (name,))
                result = cur.fetchone()
                if result:
                    return {
                        'item_id': result[0],
                        'item_name': result[1],
                        'item_price': result[2]
                    }
                return None

    @classmethod
    def all(cls):
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Menu_Items")
                results = cur.fetchall()
                items = []
                for row in results:
                    items.append({
                        'item_id': row[0],
                        'item_name': row[1],
                        'item_price': row[2]
                    })
                return items
            

