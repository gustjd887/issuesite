# Generated by Django 3.1.1 on 2020-10-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0009_auto_20201015_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='site',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='issue',
            name='site',
            field=models.CharField(choices=[('pp', '뽐뿌'), ('cl', '클리앙'), ('ou', '오유')], max_length=10),
        ),
    ]
