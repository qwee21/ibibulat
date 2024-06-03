from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'Category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

class Subcategories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    categories = models.ManyToManyField(to=Categories, verbose_name='Категория')

    class Meta:
        db_table = 'Subcategory'
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='services_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7,decimal_places=0, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(to=Subcategories, on_delete=models.CASCADE, verbose_name='Подкатегория')

    class Meta:
        db_table = 'Service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
