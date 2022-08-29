from datetime import datetime

import translit as translit
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Название оборудования', max_length=150)
    text = models.TextField(max_length=350, blank=True, null=True, default='аппарат для ультразвукового SMAS-лифтинга')
    url = models.SlugField('URL', max_length=150)
    file = models.FileField(upload_to='product_video', validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
                            blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    image = models.ImageField(verbose_name='Картинка', upload_to='product', blank=True, null=True)
    power = models.IntegerField(verbose_name='Мощьность', default=500, blank=True, null=True)
    number_of_mode = models.IntegerField(verbose_name='Число режимов', default=12, blank=True, null=True)
    views = models.IntegerField(verbose_name='Просмотры', null=True, blank=True, default=0)
    indications_and_principle_of_operation = models.TextField(verbose_name='Показания и принцип работы', blank=True,
                                                              null=True, default='Скоро будет')
    cartridges = models.CharField(max_length=450, verbose_name='Картриджи', blank=True, null=True,
                                  default='Скоро будет')
    results_of_procedures = models.CharField(max_length=450, verbose_name='Результаты процедур', blank=True, null=True,
                                             default='Скоро будет')
    features_of_the_device = models.CharField(max_length=450, verbose_name='Особенности аппарата', blank=True,
                                              default='Скоро будет', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})


class Intro(models.Model):
    name = models.CharField('Название прибора', max_length=150)
    text_title = models.TextField(max_length=350, blank=True, null=True)
    image = models.ImageField(verbose_name='Установка изображения', upload_to='intro', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True,
                                verbose_name='Продукт', help_text='Выберете к какому продукты относется интро')
    draft = models.BooleanField(verbose_name='Активна или нет', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интро'
        verbose_name_plural = 'Интро'

    # def get_absolute_url(self):
    #     return reverse('intro_detail', kwargs={'slug': self.name})


class Events(models.Model):
    title = models.CharField('Название занятия', max_length=150)
    url = models.SlugField('URL', max_length=150)
    text = models.CharField(max_length=350, blank=True, null=True, verbose_name='Краткое описание')
    data_up = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    article_date = models.DateTimeField(verbose_name='Дата мероприятия')
    training_formats = models.TextField(verbose_name='Форма обучения', blank=True, null=True,)
    description = models.TextField(blank=True, null=True, verbose_name='Основные направления')
    learning_conditions = models.TextField(blank=True, null=True, verbose_name='Условия обучения')
    views = models.IntegerField(verbose_name='Просмотры', null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.url})


# Reviews








class Schools(models.Model):
    pass

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучения'


class Partners(models.Model):
    pass

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Staff(models.Model):
    pass

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Contacts(models.Model):
    pass
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



