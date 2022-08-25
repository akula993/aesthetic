import translit as translit
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Название оборудования', max_length=150)
    text_title = models.CharField(max_length=350, blank=True, null=True)
    url = models.SlugField('URL', max_length=150)
    file = models.FileField(upload_to='product_video', blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    image = models.ImageField(verbose_name='Картинка', upload_to='product', blank=True, null=True)
    power = models.IntegerField(verbose_name='Мощьность', default=500, blank=True, null=True)
    number_of_mode = models.IntegerField(verbose_name='Число режимов', default=12, blank=True, null=True)
    views = models.IntegerField(verbose_name='Просмотры', null=True, blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})


class Intro(models.Model):
    name = models.CharField('Название прибора', max_length=150)
    text_title = models.CharField(max_length=350, blank=True, null=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='intro', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интро'
        verbose_name_plural = 'Интро'

    # def get_absolute_url(self):
    #     return reverse('intro_detail', kwargs={'slug': self.name})

# class Calendar(models.Model):
