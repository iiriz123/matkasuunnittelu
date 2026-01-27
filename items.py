import db

def add_item(destination, travel_dates, description, user_id):
    sql = """INSERT INTO items (destination, travel_dates, description, user_id) 
    VALUES (?, ?, ?, ?)"""
    db.execute(sql, [destination, travel_dates, description, user_id])

def get_items():
    sql= "SELECT id, destination FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql="""SELECT i.destination,
                  i.travel_dates,
                  i.description,
                  u.username
    from items i, users u WHERE u.id = i.user_id AND i.id = ?"""
    return db.query(sql, [item_id])[0]