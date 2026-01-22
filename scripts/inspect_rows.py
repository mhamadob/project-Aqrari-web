import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMO.settings')
import django
django.setup()

from django.db import connection

def q(sql):
    with connection.cursor() as c:
        c.execute(sql)
        return c.fetchall()

print('Counts:')
for t in ['service_provider_service_provider','property_propertys','venues_venues','venues_booking','property_booking','client_client','auth_user']:
    try:
        r = q(f"SELECT COUNT(*) FROM {t}")
        print(f" {t}: {r[0][0]}")
    except Exception as e:
        print(f" {t}: error {e}")

print('\nSample owner_id values in venues_venues:')
try:
    rows = q("SELECT id, owner_id FROM venues_venues LIMIT 20")
    for r in rows:
        print(r)
except Exception as e:
    print(' error', e)

print('\nSample owner_id values in property_propertys:')
try:
    rows = q("SELECT id, owner_id FROM property_propertys LIMIT 20")
    for r in rows:
        print(r)
except Exception as e:
    print(' error', e)
