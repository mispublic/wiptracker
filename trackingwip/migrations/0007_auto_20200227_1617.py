# Generated by Django 2.1.15 on 2020-02-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingwip', '0006_auto_20200227_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='wom',
            field=models.CharField(max_length=6, unique=True, verbose_name='Main WIP'),
        ),
    ]
