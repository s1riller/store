from django.db import models


# Create your models here.

class Bot(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    token = models.TextField()
    image = models.ImageField(upload_to='products_images')


    def __str__(self):
        return f'Бот: {self.name}'