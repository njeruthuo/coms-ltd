from django.contrib import admin
from .models import Package, Profile, Subscription


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'bundle', 'price')


@admin.register(Subscription)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('user', 'package')
