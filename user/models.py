from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    title = models.CharField(max_length=200)
    bundle = models.PositiveIntegerField(default=1000)
    image = models.URLField(max_length=2083)
    price = models.IntegerField(default=500)

    def __str__(self) -> str:
        return self.title


class Profile:
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    subscription = models.OneToOneField(
        'Subscription', on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='profile', null=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Subscription(models.Model):

    def __str__(self):
        return self.user.username+'\'s package.'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
