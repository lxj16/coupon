from django.urls import path, include
from . import views

app_name = 'couponApp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='couponHome'),
    path('checkout/', views.CheckoutView,  name='checkout'),
]