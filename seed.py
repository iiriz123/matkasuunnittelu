import random
import sqlite3
from datetime import datetime, timedelta

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM comments")

user_count = 1000
item_count = 10**5
comment_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, item_count + 1):
    user_id = random.randint(1, user_count)
    random_days = random.randint(0, 365)
    start_date = datetime.now() + timedelta(days=random_days)
    end_date = start_date + timedelta(days=1)
    sql = """INSERT INTO items (destination, start_date, end_date, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql,["country"+str(i), start_date.date(), end_date.date(), "plan"+str(i), user_id])

for i in range(1, comment_count + 1):
    user_id = random.randint(1, user_count)
    item_id = random.randint(1, item_count)
    sql = "INSERT INTO comments (comment, user_id, item_id) VALUES (?, ?, ?)"
    db.execute(sql, ["comment" + str(i), user_id, item_id])

db.commit()
db.close()
