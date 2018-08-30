# _*_  coding : utf-8  _*_
from django.conf.urls import url
from django.contrib import admin
from .views import *
urlpatterns = [
    url('^addcart',add_cart,name='add_cart'),
    url('^cartinfo',cart_info,name='catinfo'),
    url('^order',order,name='order'),
    url('^addorder',add_order,name='addorder'),
]

