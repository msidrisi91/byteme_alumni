# Generated by Django 3.0.2 on 2020-01-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200118_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
