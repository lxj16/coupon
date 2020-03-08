from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, TemplateView
from .models import Coupon, Brand, OrderItem, Order, SoldCoupon
from datetime import timedelta, date
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from couponProject.settings import EMAIL_HOST_USER
import json
from django.conf import settings
from twilio.rest import Client
from django.template.loader import get_template

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


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutView(View):
    def get(self, request):
        context = {}
        return render(request, 'couponApp/checkout.html', context)

    def post(self, request):
        if request.method == 'POST':

            data = json.loads(request.body.decode('utf-8'))

            orderItems = data['orderItems']

            #newOrder = Order(user=data['sentTo'], ordered_date=timezone.now())
            total = 0
            for item in orderItems:
                coupon_obj = Coupon.objects.get(code=item['code'])
                orderItem = OrderItem(user=data['sentTo'], coupon=coupon_obj,
                                      quantity=item['quantity'], estimatePurchaseAmount=item['estimate'])
                orderItem.save()
                # newOrder.items.add(orderItem)
                total += item['subtotal']
            
            # newOrder.total = total
            # newOrder.save()
            context = {
                'orderItems': orderItems,
                'total': total

            }
            if data['sentToType'] == 'email':
                # html_template = get_template('couponApp/email/orderEmail.html').render()
                message = f'Here is your order: {orderItems},{total}'
                send_mail(
                    subject='Your Coupon',
                    message=message,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[data['sentTo']],
                    fail_silently=False,
                )
                # message = send_mail(
                #     subject='Your Coupon',
                #     message=html_template,
                #     from_email=EMAIL_HOST_USER,
                #     recipient_list=[data['sentTo']],
                #     fail_silently=False,
                # )
            # elif data['sentToType'] == 'phone':
            #     phoneNumber = data['sentTo']
            #     message_to_broadcast = ("Your coupons here")
            #     client = Client(settings.TWILIO_ACCOUNT_SID,
            #                     settings.TWILIO_AUTH_TOKEN)

            #     client.messages.create(to=phoneNumber,
            #                            from_=7781234567,
            #                            body=message_to_broadcast)

            return render(request, 'couponApp/checkoutSuccess.html', context)


def checkoutSuccessView(request):
    return render(request, 'couponApp/checkoutSuccess.html')

def useCoupon(request, code):
    soldCoupon_obj = SoldCoupon.objects.get(code=code)
    soldCoupon_obj.used = True
    soldCoupon_obj.save()
    orderItem_obj = soldCoupon_obj.item

    context={
        'orderItem': orderItem_obj
    }

    return render(request, 'couponApp/useCoupon.html', context)


# def sendSMS(request, phoneNumber):
#     message_to_broadcast = ("Your coupons here")
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

#     client.messages.create(to=phoneNumber,
#                            from_=7781234567,
#                            body=message_to_broadcast)
#     return HttpResponse("messages sent!", 200)
