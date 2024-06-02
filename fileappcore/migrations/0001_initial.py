# Generated by Django 5.0.6 on 2024-06-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='media')),
                ('resume', models.FileField(upload_to='media')),
                ('mobileNo', models.IntegerField()),
                ('favorite_color', models.CharField(max_length=100)),
            ],
        ),
    ]