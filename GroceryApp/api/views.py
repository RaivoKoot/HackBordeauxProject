
from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ShoppingViewSet(viewsets.ModelViewSet):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
