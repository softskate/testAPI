# Generated by Django 3.2.9 on 2021-11-16 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 18, 25, 18, 73392), verbose_name='Date'),
        ),
    ]