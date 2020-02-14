from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

#coupon for sale
class Coupon(models.Model):
    companyName = models.CharField(max_length=25)
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    used = models.BooleanField(default=False)

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