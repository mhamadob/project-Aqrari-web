import os
import django
import traceback
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMO.settings')
django.setup()

from django.db import transaction
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from service_provider.models import service_provider, DeleteProfile

qs = service_provider.objects.all()
user_ids = list(qs.filter(user__isnull=False).values_list('user_id', flat=True))
print('service_provider count:', qs.count())
print('linked user ids:', user_ids)

try:
    post_delete.disconnect(DeleteProfile, sender=service_provider)
    print('Disconnected DeleteProfile signal')
except Exception as e:
    print('Disconnect error:', e)

try:
    with transaction.atomic():
        print('Attempting to delete service_provider records...')
        deleted = service_provider.objects.all().delete()
        print('service_provider delete result:', deleted)
except Exception as e:
    print('Error deleting service_provider:')
    traceback.print_exc()

try:
    if user_ids:
        with transaction.atomic():
            print('Attempting to delete User records...')
            deleted_users = User.objects.filter(id__in=user_ids).delete()
            print('User delete result:', deleted_users)
except Exception as e:
    print('Error deleting Users:')
    traceback.print_exc()

print('Done')
