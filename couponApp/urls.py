from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='couponHome'),
    #path('<slug:companyName>/', views.CouponDetailView.as_view(), name='couponDetail'),
    path('<slug:couponSlug>/', views.couponDetail, name='couponDetail'),

]