from pyexpat import model
from django.db import models
from sqlalchemy import null


class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    is_featured = models.BooleanField(default=False)
    barcode = models.CharField(max_length=13, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name