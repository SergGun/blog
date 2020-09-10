from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.TextField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Tag(models.Model):
    title = models.TextField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = CKEditor5Field('Содержание', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Загрузить фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
