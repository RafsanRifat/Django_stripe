import stripe
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from django.http import JsonResponse

from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://localhost:8000/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name':'Stubborn Attachment',
                            # 'images': ['https://i.imgur.com/EHyR2nP.png" alt="The cover of Stubborn Attachments'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
