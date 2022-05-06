from django.db import models
from django.urls import reverse
from authapp.models import User


class Cats(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='user_id')
    name = models.CharField(max_length=20, verbose_name='name')
    age = models.IntegerField(verbose_name='age')
    breed = models.CharField(max_length=20, verbose_name='breed')
    photo = models.ImageField(verbose_name='Фото', upload_to='static/cats_photos', blank=True)

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_absolute_url(self):
        return reverse('cats')
