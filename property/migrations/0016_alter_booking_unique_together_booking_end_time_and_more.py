

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_alter_booking_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('property', 'date', 'start_time', 'end_time')},
        ),
    ]
