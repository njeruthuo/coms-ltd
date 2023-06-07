from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, Profile, Subscription
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    packages = Package.objects.order_by('-price')
    return render(request, 'coms/index.html', {
        'packages': packages
    })


@login_required(login_url='login')
def home(request):
    user = request.user
    packages = Package.objects.order_by('-price')
    subscriptions = Subscription.objects.filter(user=user)
    context = {
        'subscriptions': subscriptions,
        'packages': packages,
    }
    return render(request, 'coms/home.html', context)


@login_required(login_url='login')
def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'coms/package-detail.html', {
        'package': package
    })


@login_required(login_url='login')
def package_application(request, pk):
    package = get_object_or_404(Package, pk=pk)

    if request.method == 'POST':
        user = request.user
        package = package

        if Subscription.objects.filter(user=user).exists():
            messages.error(request, 'You already have an active subscription.')
            return redirect('home')

        subscription = Subscription.objects.create(user=user, package=package)
        subscription.save()
        return redirect('home')

    return render(request, 'coms/package-application.html', {
        'package': package
    })


def subscriptions(request):
    user = request.user
    subscriptions = Subscription.objects.all()
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'coms/subscriptions.html', {
        'subscriptions': subscriptions,
        'profile': profile,
    })


@login_required(login_url='login')
def subscription_removal(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)

    if request.method == 'POST':
        subscription.delete()
        messages.warning(request, 'You deleted the package...')
        return redirect('home')

    return render(request, 'coms/remove-package.html', {
        'subscriptions': subscription
    })
