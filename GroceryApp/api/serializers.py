from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = ('shopper',
            'personal_list'
            'store',
            'pickup',
            'status')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name',
            'amount',
            'maximum_price')


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(source='items_set', many=True)

    class Meta:
        model = ShoppingList
        fields = ('author', 'items')


class RequestSerializer(serializers.ModelSerializer):
    shopping_list = ShoppingListSerializer()

    class Meta:
        model = Request
        fields = ('author',
            'shopping_list'
            'shopping',
            'pickup',
            'status')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
