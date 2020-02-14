from django.contrib import admin
from .models import Promote

# Register your models here.
class PromoteCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'startDate', 'expireDate', 'discountPercentage', 'active']
    list_filter = ['active', 'startDate', 'expireDate']
    search_fields = ['code']

admin.site.register(Promote, PromoteCodeAdmin)