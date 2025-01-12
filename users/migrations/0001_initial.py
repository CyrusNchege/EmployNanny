# Generated by Django 4.0.5 on 2023-04-17 11:12

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
            name='NannyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('id_number', models.IntegerField(default=0)),
                ('level_of_education', models.CharField(choices=[('College', 'college'), ('High School', 'high school'), ('Primary School', 'primary school')], max_length=100)),
                ('recommendation_letter', models.FileField(null=True, upload_to='recommendations/')),
                ('nationality', models.CharField(max_length=100)),
                ('availability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=100)),
                ('language', models.CharField(max_length=200)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='nanny_profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
