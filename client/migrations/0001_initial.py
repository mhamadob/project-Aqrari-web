

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='client_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('service_provider_image', models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='service_providers/')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('Prefer not to say', 'Prefer not to say')], default='Prefer not to say', max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
