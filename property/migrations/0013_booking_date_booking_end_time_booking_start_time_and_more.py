

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_booking_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(default=datetime.time(17, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertys'),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('property', 'date', 'start_time', 'end_time')},
        ),
    ]
