from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(verbose_name='user_name', unique=True, max_length=25, blank=False)
    email = models.EmailField(verbose_name='email', unique=True, blank=False)
    password = models.CharField(verbose_name='password', max_length=250, blank=False)
    is_staff = models.BooleanField(verbose_name='breeder')

    def __str__(self):
        return self.username
