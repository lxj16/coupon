from django.urls import path, include
from . import views

app_name = 'couponApp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='couponHome'),
    path('checkout/', views.CheckoutView.as_view(),  name='checkout'),
    path('checkout/success/', views.checkoutSuccessView,  name='checkoutSuccess'),
    path('use/<str:code>', views.useCoupon, name='useCoupon')
]