from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
        
#coupon for sale
class Coupon(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE),
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    #couponSlug = models.SlugField(max_length=25, default='coupon slug')
    # expireDate = models.DateTimeField()
    #used = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.discountPercentage)

#promote code for the website
class Promote(models.Model):
    code = models.CharField(max_length=50, unique=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    discountPercentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    
    def __str__(self):
        return self.code

class User(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class OrderItem(models.Model):
    item = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    expireDate = models.DateTimeField()
    used = models.BooleanField(default=False)
    purchasedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user

# # class Item(models.Model):
# #     # coupon



# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Coupon, on_delete=models.CASCADE)

