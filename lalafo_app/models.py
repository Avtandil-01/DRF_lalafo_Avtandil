from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    owner = models.CharField(max_length=32)
    phone_number = PhoneNumberField(region='KG', blank=True, null=True)
    description = models.TextField()
    address = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    product_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
