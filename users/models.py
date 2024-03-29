from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **other_fields):

        if 'password1' in other_fields:
            password = other_fields.pop('password1')
        if 'password2' in other_fields:
            other_fields.pop('password2')

        user = self.model(
            username=username,
            **other_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **other_fields)

    def create_superuser(self, username, password=None, **other_fields):
        other_fields['is_staff'] = True
        other_fields['is_superuser'] = True

        return self._create_user(username, password, **other_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, verbose_name='username', unique=True)

    first_name = models.CharField(max_length=50, blank=True, null=True,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, null=True,
                                 verbose_name='Фамилия')

    can_vote = models.BooleanField(default=False, verbose_name='Может голосовать?')

    # Django fields
    is_staff = models.BooleanField(default=False,
                                   verbose_name='Персонал сайта?')
    is_active = models.BooleanField(default=True,
                                    verbose_name='Активен?')
    date_joined = models.DateTimeField(default=timezone.now,
                                       verbose_name='Дата присоединения')
    last_login = models.DateTimeField(null=True,
                                      verbose_name='Последний вход')

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}' if self.first_name else self.username

    def get_short_name(self):
        return self.first_name or self.username

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
