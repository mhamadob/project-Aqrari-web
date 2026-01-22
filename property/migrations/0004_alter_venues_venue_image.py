
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_venues_venue_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertys',
            name='property_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
