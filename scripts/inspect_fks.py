import sqlite3

db = 'db.sqlite3'
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [r[0] for r in cur.fetchall()]

for t in tables:
    print('Table:', t)
    try:
        cur.execute(f"PRAGMA foreign_key_list('{t}')")
        rows = cur.fetchall()
        if rows:
            for r in rows:
                print('  ->', r)
        else:
            print('  -> no foreign keys')
    except Exception as e:
        print('  -> error:', e)

conn.close()
