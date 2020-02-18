from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Coupon

# Create your views here.
def index(request):

    coupons = Coupon.objects.all()

    context = {'coupons': coupons}
    return render(request, 'couponApp/main.html', context)

class HomeView(ListView):
    model = Coupon
    paginate_by = 10
    template_name = "couponApp/couponHome.html"

    def get_context_data(self, **kwargs):
        coupons = Coupon.objects.all()
        context = {'coupons': coupons}
        return context

def couponDetail(request, couponSlug):
    try:
        companyName = Coupon.objects.get(couponSlug=couponSlug).companyName
    except:
        companyName = 'not found'
    context = {'companyName': companyName}
    return render(request, 'couponApp/couponDetail.html', context)

# class CouponDetailView(DetailView):
#     model = Coupon
#     slug_field = 'couponSlug'
#     template_name = "couponApp/couponDetail.html"