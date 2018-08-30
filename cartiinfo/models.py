from django.db import models

# Create your models here.
from memberapp.models import Goods
from userinfo.models import UserInfo

ORDERSTATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'订单取消')
)

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo,db_column='user_id')
    goods = models.ForeignKey(Goods,db_column='good_id')
    ccount = models.IntegerField('数量',db_column='cart_count')
    def __str__(self):
        return self.user.uname

class Order(models.Model):
    orderNo = models.CharField('订单号',max_length=50)
    orderdatail = models.TextField('订单详情',)
    adsname = models.CharField('收件人姓名',max_length=30)
    adsphone = models.CharField('收件人号码',max_length=11)
    ads = models.CharField('地址',max_length=300)
    time = models.DateTimeField(auto_now=True)
    acot = models.IntegerField('总数')
    # 浮点数
    acount = models.DecimalField('总价',max_digits=8,decimal_places=2)
    orderstatus = models.IntegerField('订单',choices=ORDERSTATUS,default=1)
    user = models.ForeignKey(UserInfo)
    def __str__(self):
        return self.orderNo