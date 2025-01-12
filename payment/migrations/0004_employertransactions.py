# Generated by Django 4.0.5 on 2023-05-31 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0003_salarypayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deposited', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_withdrawn', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
