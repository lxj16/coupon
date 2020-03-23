from django.contrib import admin
from .models import Coupon, Promote, Order, OrderItem, Brand, Category

# Register your models here.
# class BrandInline(admin.TabularInline):
#     model = Brand
#     extra = 2

# class CouponAdmin(admin.ModelAdmin):
#     list_display = ['brand', 'discountPercentage']
#     # list_filter = ['brand']

# class PromoteCodeAdmin(admin.ModelAdmin):
#     list_display = ['code', 'startDate', 'expireDate', 'discountPercentage', 'active']
#     list_filter = ['active', 'startDate', 'expireDate']
#     search_fields = ['code']

admin.site.register(Coupon)
admin.site.register(Promote)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Brand)
admin.site.register(Category)
