from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
from django.urls import reverse

import random 
import string 
from datetime import timedelta
from django.utils import timezone

def _randomIDGenerator():
    '''
    random generation of coupon id's 
    Later, we need to change this function to follow by certain rules
    '''
    random_id = ''.join([random.choice(string.ascii_letters 
    + string.digits) for n in range(8)]) 
    return random_id

def _three_month_from_now():
    '''
    return a time that 90 days from now
    '''
    return timezone.now() + timedelta(days=90)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, default=_randomIDGenerator)
    store = models.ForeignKey('Brand', null=True, on_delete=models.CASCADE, blank = True)
    description = models.TextField()
    paymentPercentage = models.IntegerField(default=50)
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    expireDate = models.DateTimeField(default=_three_month_from_now, blank=True, null=True) #3 months from now, we need to confirm the rules
    active = models.BooleanField(default=True)
    user = models.TextField(max_length=100, null=True)
    img = models.TextField(null=True)

    def __str__(self):
        return f'{self.description} {self.discountPercentage}%'


class Brand(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=100, default='')
    coupons = models.ManyToManyField(Coupon)

    def __str__(self):
        return self.name


# promote code for the website
class Promote(models.Model):
    code = models.CharField(max_length=50, unique=True)
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    user = models.TextField(null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    used = models.BooleanField(default=False)
    estimatePurchaseAmount = models.FloatField(null=True)

    def __str__(self):
        return f'{self.item} coupon'


class Order(models.Model):
    user = models.TextField(max_length=100)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return f'{self.user} orderd {self.items}'

