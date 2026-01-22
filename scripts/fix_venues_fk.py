import sqlite3
import os
DB = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3')
con = sqlite3.connect(DB)
cur = con.cursor()
# remove venues rows with missing owner
cur.execute("DELETE FROM venues_venues WHERE owner_id NOT IN (SELECT id FROM service_provider_service_provider);")
deleted1 = cur.rowcount
# also remove any propertys rows whose owner missing (table may be property_venues or similar)
# attempt common names
try:
    cur.execute("DELETE FROM propertys_propertys WHERE owner_id NOT IN (SELECT id FROM service_provider_service_provider);")
    deleted2 = cur.rowcount
except Exception:
    deleted2 = 0
con.commit()
con.close()
print(f"Deleted {deleted1} invalid rows from venues_venues and {deleted2} from propertys_propertys (if present)")
