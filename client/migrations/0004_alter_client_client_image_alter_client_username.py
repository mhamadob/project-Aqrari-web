

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_client_service_provider_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_image',
            field=models.ImageField(blank=True, default='default_image.jpg', max_length=255, null=True, upload_to='client/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
