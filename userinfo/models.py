from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upassworld = models.CharField('密码',max_length=200,null=False)
    email = models.CharField('邮箱',max_length=50,null=False)
    phone = models.CharField('手机号',max_length=11,null=False)
    time = models.DateTimeField('注册时间',auto_now=True)
    isben = models.BooleanField('禁用',default=False)
    isdelete = models.BooleanField('删除',default=False)
    def __str__(self):
        return self.uname


class Address(models.Model):
    aname = models.CharField('收货人',max_length=50,null=False)
    ads = models.CharField('地址',max_length=300,null=False)
    phone = models.CharField('手机',max_length=11,null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE) #关联删除
    def __str__(self):
        return self.aname
