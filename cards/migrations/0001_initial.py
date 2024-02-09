# Generated by Django 4.2.9 on 2024-01-28 13:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')])),
                ('users', models.ManyToManyField(related_name='classes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cards')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('plain_name', models.CharField(max_length=50, verbose_name='Очищенное название')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст')),
                ('plain_text', models.CharField(max_length=1000, verbose_name='Очищенный текст')),
                ('mana', models.SmallIntegerField(blank=True, null=True, verbose_name='Мана')),
                ('attack', models.SmallIntegerField(blank=True, null=True, verbose_name='Атака')),
                ('health', models.SmallIntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('card_type', models.CharField(max_length=25, verbose_name='Тип карты')),
                ('race', models.CharField(blank=True, max_length=25, null=True, verbose_name='Раса')),
                ('rarity', models.CharField(max_length=25, verbose_name='Редкость')),
                ('cl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.class')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
                'ordering': ['name'],
            },
        ),
    ]
