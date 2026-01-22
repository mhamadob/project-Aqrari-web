

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_booking_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.propertys'),
        ),
    ]
