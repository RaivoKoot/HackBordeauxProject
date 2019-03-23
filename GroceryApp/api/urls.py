from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^shopping/', views.ShoppingViewSet.as_view({'get': 'list'}), name='shopping'),
    url(r'^request/', views.RequestViewSet.as_view({'get': 'list'}), name='request'),
    url(r'^shopping_list/', views.ShoppingListViewSet.as_view({'get': 'list'}), name='shopping_list'),
    url(r'^user/', views.UserViewSet.as_view({'get': 'list'}), name='user'),
    ]
