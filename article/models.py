from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(max_length=5000, verbose_name='Содержание')
    author = models.ForeignKey(User, max_length=255, verbose_name='Автор', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = CloudinaryField('image')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text[:25] + '...')
