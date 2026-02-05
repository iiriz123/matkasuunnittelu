import db

def add_item(destination, start_date, end_date, description, user_id):
    sql = """INSERT INTO items (destination, start_date, end_date, description, user_id) 
    VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [destination, start_date, end_date, description, user_id])

def get_items():
    sql= "SELECT id, destination FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql="""SELECT i.id,
                  i.destination,
                  i.start_date,
                  i.end_date,
                  i.description,
                  u.username,
                  u.id user_id
    from items i, users u WHERE u.id = i.user_id AND i.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(destination, start_date, end_date, description, item_id):
    sql = """ UPDATE items SET destination = ?,
                               start_date = ?,
                               end_date = ?,
                               description = ? WHERE id = ?"""
    db.execute(sql, [destination, start_date, end_date, description, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, destination 
             FROM items
             WHERE destination LIKE ? OR description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])