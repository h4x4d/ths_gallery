# Generated by Django 5.0.1 on 2024-03-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20240327_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='can_vote',
            field=models.BooleanField(default=False, verbose_name='Может голосовать?'),
        ),
    ]
