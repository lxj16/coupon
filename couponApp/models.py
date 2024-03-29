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


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=100, default='', blank=True)
    # coupons = models.ManyToManyField(Coupon, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, default='')
    description = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True,
                            default=_randomIDGenerator)
    # code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    store_id = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)  # company id
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, null=True, blank=True)
    category = models.TextField(max_length=100, null=True, blank=True)

    description = models.TextField()  # coupon description
    paymentPercentage = models.IntegerField(default=50)
    discountPercentage = models.TextField(
        max_length=3, null=True, blank=True)  # coupon  %/
    # 3 months from now, we need to confirm the rules  #expiry date
    expireDate = models.DateTimeField(
        default=_three_month_from_now, blank=True, null=True)
    used = models.BooleanField(default=False)
    user = models.TextField(max_length=100, null=True, blank=True)
    img = models.TextField(null=True, blank=True)  # coupon image

    # new:
    country = models.TextField(max_length=50, null=True, blank=True)
    address = models.TextField(
        max_length=200, null=True, blank=True)  # address,post code

    # i.e. vancouver, toronto, richmond
    service_area = models.TextField(max_length=200, null=True, blank=True)
    telephone = models.TextField(blank=True, help_text='Contact phone number')
    website = models.TextField(max_length=50, null=True, blank=True)
    email = models.TextField(max_length=254, null=True, blank=True)
    fax = models.TextField(
        help_text='Contact phone number', null=True, blank=True, default=False)
    term_of_use = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        # note: There is a bug with data import, the discountPercentage shoUld be an integer but not string, for now, use paymentPercentage to demo the functionality
        # return f'{self.store_id} - {self.description} - {self.discountPercentage}%'
        return f'{self.store_id} - {self.description} - {self.paymentPercentage}%'


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
        return f'{self.user}\'s coupon'


class Order(models.Model):
    user = models.TextField(max_length=100)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(null=True)
    total = models.FloatField(null=True)

    def __str__(self):
        return f'{self.user} orderd {self.items}'


class SoldCoupon(models.Model):
    code = models.CharField(max_length=50, unique=True,
                            default=_randomIDGenerator)
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
