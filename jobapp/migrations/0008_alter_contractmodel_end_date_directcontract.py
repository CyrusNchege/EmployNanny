# Generated by Django 4.2 on 2023-04-29 06:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_nannydetails_age_bracket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0007_alter_contractmodel_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 29, 6, 47, 12, 98813, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='DirectContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('job_description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('completed', 'Completed'), ('terminated', 'Terminated')], default='pending', max_length=100)),
                ('amount_to_receive', models.IntegerField()),
                ('company_commission', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nanny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.nannydetails')),
            ],
        ),
    ]
