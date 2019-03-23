from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="friendship_creator_set",
                                on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set",
                                on_delete=models.CASCADE)


class ShoppingList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=500)
    amount = models.CharField(max_length=100)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    maximum_price = models.DecimalField(max_digits=6, decimal_places=2)


class Shopping(models.Model):
    STATUS = (
        ('p', 'Pending'),
        ('f', 'Finished'),
    )

    shopper = models.ForeignKey(User, on_delete=models.CASCADE)
    personal_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    store = models.CharField(max_length=100)
    request_deadline = models.DateTimeField()
    pickup = models.DateTimeField() # blank=True, null=True
    status = models.CharField(max_length=2, choices=STATUS, default='p')


class Request(models.Model):
    STATUS = (
        ('a', 'Accepted'),
        ('d', 'Declined'),
        ('p', 'Pending'),
        ('f', 'Finished'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, null=True)
    maximum_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=2, choices=STATUS, default='p')
