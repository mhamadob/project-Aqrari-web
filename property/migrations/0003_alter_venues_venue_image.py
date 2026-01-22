

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_venues_venue_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertys',
            name='property_image',
            field=models.ImageField(blank=True, default='assets/default.jpg', null=True, upload_to='assets/'),
        ),
    ]
