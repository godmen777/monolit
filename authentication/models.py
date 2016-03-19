# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')


        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), 
            username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.is_active = True
        account.is_staff = True
        account.save()

        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    backend = 'django.contrib.auth.backends.ModelBackend'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = u"Аккаунт"
        verbose_name_plural = u"Аккаунты"

    def __unicode__(self):
        return self.username

    # def get_full_name(self):
    #     return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class PerformerProfile(models.Model):
    account = models.OneToOneField(Account, related_name='performer_of_account')
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = u"Профиль Исполнителя"
        verbose_name_plural = u"Профили Исполнителей"

    def __unicode__(self):
        return self.first_name

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])


class CustomerProfile(models.Model):
    account = models.OneToOneField(Account, related_name='customer_of_account')
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = u"Профиль Заказчика"
        verbose_name_plural = u"Профили Заказчиков"

    def __unicode__(self):
        return self.first_name

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])
