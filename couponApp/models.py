from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
from django.urls import reverse


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    paymentPercentage = models.IntegerField(default=50)
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    expireDate = models.DateTimeField() #3months
    used = models.BooleanField(default=False)
    user = models.TextField(max_length=100)
    img = models.TextField()

    def __str__(self):
        return f'{self.description} {self.discountPercentage}%'


class Brand(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=100, default='')
    coupon = models.ManyToManyField(Coupon)

    def __str__(self):
        return self.name


# promote code for the website
class Promote(models.Model):
    code = models.CharField(max_length=50, unique=True)
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    user = models.TextField()
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # expireDate = models.DateTimeField()
    used = models.BooleanField(default=False)
    estimatePurchaseAmount = models.FloatField()

    def __str__(self):
        return f'{self.item} coupon'


class Order(models.Model):
    user = models.TextField(max_length=100)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    total = models.FloatField()

    def __str__(self):
        return f'{self.user} orderd {self.items}'

