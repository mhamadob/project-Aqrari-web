

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_client_service_provider_image_and_more'),
        ('property', '0009_alter_venues_name_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.propertys'),
        ),
    ]
