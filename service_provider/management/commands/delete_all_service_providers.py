from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models.signals import post_delete
from django.contrib.auth.models import User

from service_provider.models import service_provider, DeleteProfile
from django.conf import settings
import sqlite3


class Command(BaseCommand):
    help = "Delete all service_provider accounts (and their linked User via post_delete signal)."

    def add_arguments(self, parser):
        parser.add_argument(
            '--yes',
            action='store_true',
            help='Confirm deletion without prompt',
        )

    def handle(self, *args, **options):
        if not options.get('yes'):
            confirm = input("Are you sure you want to delete ALL service_provider accounts? Type 'yes' to confirm: ")
            if confirm.strip().lower() != 'yes':
                self.stdout.write(self.style.NOTICE('Aborted. No changes made.'))
                return

        qs = service_provider.objects.all()
        count = qs.count()
        if count == 0:
            self.stdout.write('No service_provider records found.')
            return

        # Temporarily disconnect the post_delete signal that attempts to delete the User
        disconnected = False
        try:
            post_delete.disconnect(DeleteProfile, sender=service_provider)
            disconnected = True
        except Exception:
            pass

        # Collect related user IDs; delete service_provider records first (signal disconnected),
        # then delete the linked Users to avoid FK constraint errors.
        user_ids = list(qs.filter(user__isnull=False).values_list('user_id', flat=True))

        try:
            with transaction.atomic():
                service_provider.objects.all().delete()
                if user_ids:
                    User.objects.filter(id__in=user_ids).delete()
        except Exception as e:
            # attempt sqlite raw fallback if transaction failed due to FK constraints
            self.stdout.write(self.style.WARNING(f'ORM delete failed: {e}'))
            engine = settings.DATABASES.get('default', {}).get('ENGINE', '')
            if 'sqlite3' in engine:
                db_name = settings.DATABASES['default'].get('NAME')
                if db_name:
                    try:
                        conn = sqlite3.connect(db_name)
                        c = conn.cursor()
                        c.execute('PRAGMA foreign_keys = OFF;')
                        c.execute('DELETE FROM service_provider_service_provider;')
                        if user_ids:
                            ids_csv = ','.join(str(int(i)) for i in user_ids)
                            c.execute(f'DELETE FROM auth_user WHERE id IN ({ids_csv});')
                        conn.commit()
                        c.execute('PRAGMA foreign_keys = ON;')
                        conn.close()
                        self.stdout.write(self.style.SUCCESS('SQLite fallback: raw deletions completed.'))
                    except Exception as e2:
                        self.stdout.write(self.style.ERROR(f'SQLite fallback failed: {e2}'))
            else:
                self.stdout.write(self.style.ERROR('ORM delete failed and non-sqlite DB; manual cleanup required.'))

        # reconnect the signal if we removed it
        if disconnected:
            from service_provider.models import DeleteProfile as _DeleteProfile
            post_delete.connect(_DeleteProfile, sender=service_provider)

        self.stdout.write(self.style.SUCCESS(f'Deleted {count} service_provider records (ORM attempt).'))

        # If we reach here but commits failed due to sqlite FK issues elsewhere, offer a sqlite fallback.
        engine = settings.DATABASES.get('default', {}).get('ENGINE', '')
        if 'sqlite3' in engine:
            db_name = settings.DATABASES['default'].get('NAME')
            if db_name:
                try:
                    conn = sqlite3.connect(db_name)
                    c = conn.cursor()
                    c.execute('PRAGMA foreign_keys = OFF;')
                    c.execute('DELETE FROM service_provider_service_provider;')
                    if user_ids:
                        ids_csv = ','.join(str(int(i)) for i in user_ids)
                        c.execute(f'DELETE FROM auth_user WHERE id IN ({ids_csv});')
                    conn.commit()
                    c.execute('PRAGMA foreign_keys = ON;')
                    conn.close()
                    self.stdout.write(self.style.SUCCESS('SQLite fallback: raw deletions completed.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'SQLite fallback failed: {e}'))
