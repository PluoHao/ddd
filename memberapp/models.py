from django.db import models

# Create your models here.

class GoodType(models.Model):
    title = models.CharField('分类名称',max_length=30,null=False)
    desc = models.CharField('描述',max_length=300,default='商品描述')
    isdelete = models.BooleanField('删除',default=False)
    def __str__(self):
        return self.title


class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    # 小数点价格
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    desc = models.CharField('描述',max_length=200,default='商品描述')
    unit = models.CharField('单位',max_length=30)
    picture = models.ImageField('商品图片路径',upload_to='static/images/goods')
    detail = models.CharField('商品详情',max_length=1000,default='商品详情')
    isdelete = models.BooleanField('删除',default=False)
    type = models.ForeignKey(GoodType)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/detail/?goodid={}'.format(self.id)



