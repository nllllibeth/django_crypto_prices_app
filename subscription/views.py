from django.shortcuts import render

# Create your views here.


def get_subscription_page(request):
    return render(request, "subscription/subscription.html")