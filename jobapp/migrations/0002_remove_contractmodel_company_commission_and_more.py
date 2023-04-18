# Generated by Django 4.0.5 on 2023-04-18 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_employerprofile'),
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractmodel',
            name='company_commission',
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('completed', 'Completed'), ('terminated', 'Terminated')], default='pending', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.jobmodel')),
                ('nanny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.nannydetails')),
            ],
        ),
    ]
