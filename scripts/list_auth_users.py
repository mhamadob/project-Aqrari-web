import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMO.settings')
import django
django.setup()
from django.contrib.auth.models import User

users = User.objects.all().order_by('id')
print('Total users:', users.count())
print('id | username | is_superuser | is_staff | is_active')
for u in users:
    print(f"{u.id} | {u.username!r} | {u.is_superuser} | {u.is_staff} | {u.is_active}")

print('\nSuperusers:')
for u in users.filter(is_superuser=True):
    print(f"{u.id} | {u.username!r}")

print('\nStaff users:')
for u in users.filter(is_staff=True):
    print(f"{u.id} | {u.username!r}")
