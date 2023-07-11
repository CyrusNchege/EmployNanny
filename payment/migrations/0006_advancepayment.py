# Generated by Django 4.0.5 on 2023-06-22 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_nannydetails_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0022_alter_contractmodel_end_date'),
        ('payment', '0005_salarypayment_direct_contract_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.contractmodel')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nanny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.nannydetails')),
            ],
        ),
    ]