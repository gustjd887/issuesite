# Generated by Django 3.1.1 on 2020-10-05 00:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0006_auto_20201005_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='rank',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
