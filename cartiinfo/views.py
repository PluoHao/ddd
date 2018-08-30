import datetime
from django.shortcuts import render
from pymysql import DatabaseError

from .models import *

from userinfo import *

from userinfo.models import Address

from memberapp import *

import logging

import json

from django.http import HttpResponse
# Create your views here.

 #购物车的实现
def add_cart(request):
    #获取前端数据（商品id。商品数量）
    #获取用户id
    #查询
    #存
    #返回
    # 声明一个新的购物车
    # 获取前端数据
    #获取用户id
    #查询用户
    #查询商品
    #判断商品是否存在
    #查询购物车中该用户是否有此商品
    #商品数量转为int
    #如果又加上相应数量的商品
    #没有直接保存
    # 方法一
    new_cart = CartInfo()
    goods_id = request.GET.get('goodid')
    good_count = request.GET.get('gcount')
    user_id = request.session.get('user_id')
    good_ = Goods.objects.filter(id=goods_id)
    user_ = UserInfo.objects.get(id=user_id)
    print(good_count,goods_id,user_id)
    if len(good_)  > 0:

        new_cart.user = user_
        new_cart.goods = good_[0]
    else:
        content = {'static':"OK",'text':"无该商品"}
        return HttpResponse(json.dumps(content))
        # return render(request,'index.html')
    new_cart.ccount = int(good_count)
    print(new_cart.ccount)
    try:
        oldgo = CartInfo.objects.filter(user_id=user_id,goods_id=goods_id)
        print(goods_id)
        if len(oldgo) > 0:
            oldgo[0].ccount = oldgo[0].ccount + new_cart.ccount
            oldgo[0].save()
        else:
            new_cart.save()
    except DatabaseError as e:
        logging.warning(e)
    # return render(request,'index.html')
    content = {'static':"OK",'text':"添加成功"}
    return HttpResponse(json.dumps(content))


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goods = CartInfo.objects.filter(user_id=user_id)
    return render(request,'cart.html',{'find_goods':find_goods})

#订单
def order(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {'adss':adss}
    return render(request,'order.html',content)

def add_order(request):
    user_id = request.session.get('user_id')
    orderdetail = request.POST.get('acot')
    adsname = request.POST.get('adsname')
    adsphone = request.POST.get('adsphone')
    ads = request.POST.get('ads')
    acot = 2
    acount = 22.00
    orderNo = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        user = UserInfo.objects.get(id=user_id)
        order = Order.objects.create(orderNo=orderNo,orderdatail=orderdetail,adsname=adsname,adsphone=adsphone,ads=ads,user=user,acount=acount,acot=2)
    except DatabaseError as e:
        logging.warning(e)
    content = {"static":"ok"}

    return HttpResponse(json.dumps(content))


# 清空购物车
def delete_cart(request):
    user_id = request.session.get('user.id')
    cart_id = request.GET.get('cart_id')
    try:
        delcart = CartInfo.objects.filter(user_id=user_id,id=cart_id)
        delcart.delete()
    except DatabaseError as e:
        logging.warning(e)
    content = {"static":"ok","msg":"删除成功"}
    return HttpResponse(json.dumps(content))