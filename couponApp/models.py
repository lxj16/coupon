from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

#coupon for sale
class Coupon(models.Model):
    companyName = models.CharField(max_length=25, )
    couponSlug = models.SlugField(max_length=25, default='coupon slug')
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    used = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.companyName

#promote code for the website
class Promote(models.Model):
    code = models.CharField(max_length=50, unique=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    
    def __str__(self):
        return self.code

# # class Item(models.Model):
# #     # coupon
# class User(models.Model):
#     email = models.EmailField()
#     # order = Many


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Coupon, on_delete=models.CASCADE)

