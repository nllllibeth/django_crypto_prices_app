from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Currency
from .business_logic import update_currency_model


def get_currencies(request):
    page_name = "Cryptocurrency Prices"
    currencies = Currency.objects.all()
    for currencyObj in currencies:
        currencyObj = update_currency_model(currencyObj)
    context = {'page_name':page_name, 'currencies': currencies}
    return render(request, 'currencies/currencies.html', context)

def get_currency(request, pk):
    page_name = "Currency Data"
    currencyObj = Currency.objects.get(id=pk)
    id = currencyObj.id
    currencyObj_updated = update_currency_model(currencyObj)

    is_favourite = False
    if currencyObj.favourite.filter(id = request.user.id).exists():
        is_favourite = True

    context = {
        'page_name':page_name, 
        'pk':pk, 
        'currency' : currencyObj_updated, 
        'id' : id,
        'is_favourite' : is_favourite}
    return render(request, 'currencies/single_currency.html', context)


@login_required(login_url='login')
def favourite_view(request, pk):
    currency = get_object_or_404(Currency, id=request.POST.get('currency_id'))
    if currency.favourite.filter(id = request.user.id).exists():
        currency.favourite.remove(request.user)
    else:
        currency.favourite.add(request.user)
    return HttpResponseRedirect(reverse('currency', args=[str(pk)]))


@login_required(login_url='login')  
def render_favourites(request):
    user = request.user
    favourite_currencies = user.favourite.all()
    context = {'favourite_currencies' : favourite_currencies}
    return render(request, 'currencies/favourites.html', context)
