# Generated by Django 5.0.1 on 2024-02-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vote', '0002_alter_stage_options_alter_vote_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votecard',
            name='boost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Бонус'),
        ),
    ]
