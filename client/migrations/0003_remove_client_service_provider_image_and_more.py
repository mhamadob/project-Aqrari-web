

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_client_profile_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='service_provider_image',
        ),
        migrations.AddField(
            model_name='client',
            name='client_image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='client/'),
        ),
    ]
