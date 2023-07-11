# Generated by Django 4.0.5 on 2023-06-30 12:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0025_alter_contractmodel_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 30, 12, 40, 49, 381048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='duration',
            field=models.CharField(choices=[('Less than 6 months', 'less than 6 months'), ('1 - 2 Years', '1 - 2 years'), ('3 -6 years', '3 - 6 years'), ('More than 7 years', 'more than 7 years')], default='1 - 2 years', max_length=100),
        ),
    ]