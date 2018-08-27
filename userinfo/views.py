import logging

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymysql import DatabaseError

from .models import *
# Create your views here.


def register_in(request):
    return render(request,'register.html')




# 注册
# 思路
'''判断提交方式是否为post
声明一个用户
获取前端用户名
查询用户
判断用户长度
如果大于零，返回注册页
提示用户名已存在
判断两次密码是否一致
如果不一致返回注册页
提示两次密码不一致
对密码加密 make_password(要加密的内容,'abc','pbkdf2_sha1')
保存用户信息
返回首页
'''
def register_(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.uname = request.POST.get('user-name')
        a = UserInfo.objects.filter(uname=new_user)
        if len(a) > 0:
            return render(request,'register.html',{"users":"该用户已存在"})
        if request.POST.get('user_password') != request.POST.get('user_cpwd'):
            return render(request,'register.html',{"message":"密码输入不一致"})
        new_user_pwd = make_password(request.POST.get('user_password'),'abc','pbkdf2_sha1')
        new_user.upassworld = new_user_pwd
        new_user.email = request.POST.get('user_email')
        new_user.phone = request.POST.get("user_phone")
        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
            # 跳转首页
        # return HttpResponse(request,user.uname)
        return redirect('user/login')
    return redirect('user/register')
    # 获取注册信息

    # 判断用户是否存在
    # 注册用户
    # 返回页面

# 登录
def login(request):
    return render(request,'login.html')

#登录验证
def login_(request):
    if request.method == 'POST':
        user = UserInfo()
        user.uname = request.POST.get('user-name')
        user.upassworld = request.POST.get('user_password')
        try:
            print(user.uname)
            find_user = UserInfo.objects.filter(uname=user.uname)
            if len(find_user) <= 0:
                return render(request,'login.html',{"users":"用户名错误"})
            if not check_password(user.upassworld,find_user[0].upassworld):
                return render(request,'login.html',{"message":"密码错误"})
        except DatabaseError as e:
            logging.warning(e)
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = find_user[0].uname
        return redirect('/')
    return redirect('user/login')

def address(request):
    return render(request,'address.html')

#添加地址表
def add_ads(request):
    #获取用户ID(session中获取)
    if request.method == 'POST':
        add = Address()
        add.aname = request.POST.get('username')
        add.phone = request.POST.get('userphone')
        add.ads = request.POST.get('user.province')+request.POST.get('user.city')+request.POST.get('user.area')+request.POST.get('useraddress')
        ar = request.session['user_name']
        d1 = UserInfo.objects.get(uname=ar)
        add.user = d1
        Shen = request.POST.get('user.area')
        try:
            if Shen == '市辖区':
                return render(request,'address.html',{'message':'未选择区'})
            add.save()
        except DatabaseError as e:
            logging.warning(e)
        return redirect('/')
    return redirect('user/address')
    #获取前端页面传来的信息（姓名，地址）
    #对数据库进行增加操作
    #返回页面

def user_ads(request):
    # 一对多的正向查询
    try:
        Usename = request.session['user_id']
    except KeyError:
        return redirect('/user/login')
    name = Address.objects.filter(user=Usename)
    # Uname = name.user.uname
    # all = Address.objects.all()
    # print(len(all))
    return render(request,'Uselect_address.html',locals())

    # 获取用户ID/
    # 查询数据库中Address表中该用户id的数据
    #返回页面

def delete_ads(request):
    # 获取用户ID
    Use = request.session['user_id']
    adsid = request.GET.get('deletes')
    try:
        delads = Address.objects.get(id=adsid,user_id=Use)
        delads.delete()
    except DatabaseError as e:
        logging.warning(e)
    return redirect('/user/Saddres')
    # 获取地址id
    # 查询该数据
    # 删除该数据
    # 返回页面