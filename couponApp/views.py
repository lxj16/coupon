from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Coupon, Brand, OrderItem, Order
from datetime import timedelta, date
from django.utils import timezone

# Create your views here.
def index(request):

    coupons = Coupon.objects.all()

    context = {'coupons': coupons}
    
    return render(request, 'couponApp/main.html', context)

class HomeView(TemplateView):
    template_name = "couponApp/couponHome.html"
    def get_context_data(self, *args):
        brands = Brand.objects.all()
        context = {
            'brands': brands
            }
        print(brands)
        return context
        # return render(request, self.template_name, context)

def couponDetail(request, couponCode):
    try:
        storeName = Coupon.objects.get(code=couponCode).store
    except:
        storeName = 'not found'
    context = {'storeName': storeName}
    return render(request, 'couponApp/couponDetail.html', context)

class CheckoutView(View):
    template_name = "couponApp/checkout.html"
    def get(self, request):
        # try:
        #     order = Order.objects.get(user=User.objects.get(pk=1))
        # except:
        #     order = []
        
        context = {
            # 'order': order
            }
        return render(request, self.template_name, context)
# class CouponDetailView(DetailView):
#     model = Coupon
#     slug_field = 'couponSlug'
#     template_name = "couponApp/couponDetail.html"