

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_client_client_image_alter_client_username'),
        ('property', '0018_alter_booking_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertys',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_properties', to='client.client'),
        ),
    ]
