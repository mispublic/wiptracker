# Generated by Django 2.1.15 on 2020-02-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingwip', '0007_auto_20200227_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='customer',
            field=models.CharField(default='', max_length=30, verbose_name='Customer'),
        ),
    ]
