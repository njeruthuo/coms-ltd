from django.shortcuts import render


def home(request):
    return render(request, 'crm/dashboard.html')


def products(request):
    return render(request, 'crm/products.html')


def customer(request):
    return render(request, 'crm/customer.html')
