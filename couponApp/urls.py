from django.urls import path, include
from . import views

app_name = 'couponApp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='couponHome'),
    #path('<slug:companyName>/', views.CouponDetailView.as_view(), name='couponDetail'),
    path('<slug:couponSlug>/', views.couponDetail, name='couponDetail'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout')

]