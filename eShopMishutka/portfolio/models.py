from django.db import models

# Create your models here.
class PortfolioExample(models.Model):
    name = models.CharField(verbose_name='название примера работ', max_length=128, unique=True)
    image = models.ImageField(upload_to='portfolio/portfolio_images', blank=True)
    description = models.TextField(verbose_name='описание примера работ', blank=True)

    def __str__(self):
        return '{}'.format(self.name)