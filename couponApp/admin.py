from django.contrib import admin
from .models import Coupon, Promote

# Register your models here.
class CouponAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'expireDate', 'discountPercentage', 'used']
    list_filter = ['companyName', 'expireDate', 'used']
    search_fields = ['companyName']
class PromoteCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'startDate', 'expireDate', 'discountPercentage', 'active']
    list_filter = ['active', 'startDate', 'expireDate']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)
admin.site.register(Promote, PromoteCodeAdmin)