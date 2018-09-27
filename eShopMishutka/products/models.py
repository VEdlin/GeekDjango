from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=128, unique=True)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=128, blank=True)
    description = models.TextField(verbose_name='Полное описание', blank=True)
    charact = models.TextField(verbose_name='Характеристики товара', blank=True)
    image = models.ImageField(upload_to='products/products_images', blank=True)

    def __str__(self):
        return '{}'.format(self.name)