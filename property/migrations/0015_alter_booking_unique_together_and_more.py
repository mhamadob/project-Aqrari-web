

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_alter_booking_date_alter_booking_end_time_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('property', 'date')},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_time',
        ),
    ]
