from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    if created:
        pass
