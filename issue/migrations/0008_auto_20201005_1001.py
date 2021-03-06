# Generated by Django 3.1.1 on 2020-10-05 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0007_auto_20201005_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='rank',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='issue',
            name='site',
            field=models.ForeignKey(choices=[('pp', '뽐뿌'), ('cl', '클리앙'), ('ou', '오유')], max_length=10, on_delete=django.db.models.deletion.CASCADE, to='issue.community'),
        ),
    ]
