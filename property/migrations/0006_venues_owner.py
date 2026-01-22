

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0002_alter_service_provider_user'),
        ('property', '0005_alter_venues_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertys',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_provider.service_provider'),
        ),
    ]
