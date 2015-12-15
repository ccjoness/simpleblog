from django.db import models
from django.contrib.auth.models import User


def upload_handler(instance, filename):
    return "{author}/{date}/{file}".format(author=instance.author, date=instance.date, file=filename)


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=75)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=75)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to=upload_handler, blank=True)

    def __str__(self):
        return self.title
