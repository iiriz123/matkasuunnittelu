import db

def item_count():
    sql = "SELECT COUNT(id) FROM items"
    return db.query(sql)[0][0]

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)
    
    return classes

def add_item(destination, start_date, end_date, description, user_id, classes):
    sql = """INSERT INTO items (destination, start_date, end_date, description, user_id) 
    VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [destination, start_date, end_date, description, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])
    return item_id

def add_comment(item_id, user_id, comment):
    sql = """INSERT INTO comments (item_id, user_id, comment) 
    VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, comment])

def get_comments(item_id):
    sql = """SELECT comments.comment, users.id user_id, users.username
             FROM comments, users
             WHERE comments.item_id = ? AND comments.user_id = users.id
             ORDER BY comments.id DESC"""
    return db.query(sql, [item_id])

def get_images(item_id):
    sql = "SELECT id FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image from images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND item_id = ?"
    db.execute(sql, [image_id, item_id])

def get_classes(item_id):
    sql= "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items(page, page_size):
    sql= """SELECT items.id, items.destination, users.id user_id, users.username,
                   COUNT(comments.id) comment_count  
            FROM items JOIN users ON items.user_id = users.id
                       LEFT JOIN comments ON items.id = comments.item_id
            GROUP BY items.id
            ORDER BY items.id DESC
            LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

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

def update_item(destination, start_date, end_date, description, item_id, classes):
    sql = """ UPDATE items SET destination = ?,
                               start_date = ?,
                               end_date = ?,
                               description = ? WHERE id = ?"""
    db.execute(sql, [destination, start_date, end_date, description, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def remove_item(item_id):
    sql = "DELETE FROM comments WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM images WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT items.id, items.destination, users.id user_id, users.username,
                   COUNT(comments.id) comment_count  
            FROM items JOIN users ON items.user_id = users.id
                       LEFT JOIN comments ON items.id = comments.item_id
            WHERE destination LIKE ? OR description LIKE ?
            GROUP BY items.id
            ORDER BY items.id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])