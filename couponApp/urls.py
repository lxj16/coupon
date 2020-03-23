from django.urls import path, include
from . import views

app_name = 'couponApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('coupons/', views.HomeView.as_view(), name='coupons'),
    path('coupons/<str:category>',
         views.couponByCategory, name='couponByCategory'),
    path('checkout/', views.CheckoutView.as_view(),  name='checkout'),
    path('checkout/success/', views.checkoutSuccessView,  name='checkoutSuccess'),
    path('use/<str:code>', views.useCoupon, name='useCoupon'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]
