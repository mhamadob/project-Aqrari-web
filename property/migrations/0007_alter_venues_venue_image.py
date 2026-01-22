
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_venues_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertys',
            name='property_image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='images/'),
        ),
    ]
