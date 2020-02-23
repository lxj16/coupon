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
        return context
        # return render(request, self.template_name, context)

def CheckoutView(request):
    context = {
        
        }
    return render(request, 'couponApp/checkout.html',context)
