# _*_  coding : utf-8  _*_
from django.conf.urls import url
from .views import *
urlpatterns = [
    # 注册
    url('^register/$',register_in,name='register'),
    #注册验证
    url('^registerin/$',register_,name='register_sn'),
    # 登录
    url('^login/$',login,name='login'),
    #登录验证
    url('^loginfo/$',login_,name='logins'),
    #地址
    url('^address/$',address,name='address'),
    #地址注册
    url('^address_in/$',add_ads,name='address_in'),
    # 查看地址
    url('^Saddres/$',user_ads,name='Saddres'),
    #删除地址
    url('^delete/$',delete_ads,name='delete'),
]
