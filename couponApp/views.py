from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Coupon, Brand, OrderItem, Order

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
        # coupons = list(brand.coupon.all())
        # print('hahaha')
        # print(coupons)
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

def add_to_cart(request, discountPercentage):
    item = get_object_or_404(Coupon, discountPercentage=discountPercentage)
    order_item = OrderItem.objects.create(item=item)
    order = Order.objects.create()
    order.items.add(order_item)

    return redirect('couponApp:couponHome')

class CheckoutView(View):
    template_name = "couponApp/checkout.html"
    print('checkout')
    def get(self, request):
        brands = Brand.objects.all()
        # coupons = list(brand.coupon.all())
        # print('hahaha')
        # print(coupons)
        context = {
            'brands': brands
            }
        return render(request, self.template_name, context)
# class CouponDetailView(DetailView):
#     model = Coupon
#     slug_field = 'couponSlug'
#     template_name = "couponApp/couponDetail.html"