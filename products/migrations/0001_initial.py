# Generated by Django 4.1 on 2022-08-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название оборудования')),
                ('text_title', models.CharField(max_length=350)),
                ('url', models.SlugField(max_length=150, verbose_name='URL')),
                ('file', models.FileField(blank=True, null=True, upload_to='product_video')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product', verbose_name='Картинка')),
                ('power', models.IntegerField(default=500, verbose_name='Мощьность')),
                ('number_of_mode', models.IntegerField(default=12, verbose_name='Число режимов')),
            ],
        ),
    ]
