# Generated by Django 3.2.9 on 2021-11-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(verbose_name='Date')),
                ('views', models.IntegerField(verbose_name='Views')),
                ('clicks', models.IntegerField(verbose_name='Clicks')),
                ('cost', models.FloatField(verbose_name='Cost')),
            ],
        ),
    ]
