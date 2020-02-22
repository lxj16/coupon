from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Coupon, Brand, OrderItem, Order, User
from datetime import timedelta, date
from django.utils import timezone

# Create your views here.
def index(request):

    coupons = Coupon.objects.all()

    context = {'coupons': coupons}
    
    return render(request, 'couponApp/main.html', context)

class HomeView(TemplateView):
    template_name = "couponApp/couponHome.html"
    print('home')
    def get_context_data(self, *args):
        brands = Brand.objects.all()
        context = {
            'brands': brands
            }
        return context
        # return render(request, self.template_name, context)

def couponDetail(request, couponSlug):
    try:
        companyName = Coupon.objects.get(couponSlug=couponSlug).companyName
    except:
        companyName = 'not found'
    context = {'companyName': companyName}
    return render(request, 'couponApp/couponDetail.html', context)

def add_to_cart(request, slug):
    item = get_object_or_404(Coupon, slug=slug)
    expireDate =  date.today() + timedelta(days=10)
    orderItem = OrderItem.objects.get_or_create(item=item, expireDate=expireDate)
    demoUser = User.objects.get(pk=1)
    order_query = Order.objects.filter(user=demoUser)

    if order_query.exists():
        order = order_query[0]
        if order.items.filter(item__slug=item.slug).exists():
            orderItem.quantity += 1
            orderItem.save()
        else:    
            order.items.add(orderItem)
    else:
        order = Order.objects.create(user=User.objects.get(pk=1))

    return redirect('couponApp:couponHome')

def remove_from_cart(request, slug):
    item = get_object_or_404(Coupon, slug=slug)
    demoUser = User.objects.get(pk=1)
    order_query = Order.objects.filter(user=demoUser)

    if order_query.exists():
        order = order_query[0]
        if order.items.filter(item__slug=item.slug).exists():
            orderItem= OrderItem.objects.filter(item=item, ordered=False)[0]
            order.items.remove(orderItem)

    return redirect('couponApp:couponHome')

class CheckoutView(View):
    template_name = "couponApp/checkout.html"
    print('checkout')
    def get(self, request):
        try:
            order = Order.objects.get(user=User.objects.get(pk=1))
        except:
            order = []
        
        context = {
            'order': order
            }
        return render(request, self.template_name, context)
# class CouponDetailView(DetailView):
#     model = Coupon
#     slug_field = 'couponSlug'
#     template_name = "couponApp/couponDetail.html"