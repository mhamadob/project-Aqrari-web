import sqlite3
import os
DB = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
con = sqlite3.connect(DB)
cur = con.cursor()
# remove bookings referencing missing venues
cur.execute("DELETE FROM venues_booking WHERE venue_id NOT IN (SELECT id FROM venues_venues);")
deleted = cur.rowcount
con.commit()
con.close()
print(f"Deleted {deleted} invalid rows from venues_booking")
