import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
con = sqlite3.connect(DB)
cur = con.cursor()
# delete rows in auth_user_groups referencing missing users
cur.execute("DELETE FROM auth_user_groups WHERE user_id NOT IN (SELECT id FROM auth_user);")
deleted = cur.rowcount
con.commit()
con.close()
print(f"Deleted {deleted} invalid rows from auth_user_groups")
