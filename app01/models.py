from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Course(models.Model):
    '''
    普通课程
    '''
    title = models.CharField(max_length=32)
    # 用于GenericForeignKey反向查询，不会生成表字段
    price_policy_list = GenericRelation('PricePolicy')


class DegreeCourse(models.Model):
    '''
    学位课程
    '''
    title = models.CharField(max_length=32)
    # 用于GenericForeignKey反向查询，不会生成表字段
    # price_policy_list = GenericRelation('PricePolicy')


class PricePolicy(models.Model):
    '''
    价格策略
    '''
    price = models.IntegerField()
    period = models.IntegerField()

    # table_name = models.CharField(verbose_name='关联的表名称')
    # obiect_id = models.CharField(verbose_name='关联表中数据行的ID')
    content_type = models.ForeignKey(ContentType, verbose_name='关联普通课或者学位课', on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name='关联普通课或者学位课的课程ID')
    # 帮助你快速实现content_type操作
    content_object = GenericForeignKey('content_type', 'object_id')


'''
需求：
1、为学位课“python全栈”添加一个价格策略：一个月 9.9
    
# 实现方式一：不使用content_type操作，即PricePolicy表中不加content_object = GenericForeignKey('content_type', 'object_id')
obj = DegreeCourse.objects.filter(title='python全栈').first()
cobj = ContentType.objects.filter(model='degreecourse').first()
PricePolicy.objects.create(price=9.9, period=30, content_type=cobj.id, object_id=obj.id)

# 实现方式二：使用content_type操作，即PricePolicy表中加content_object = GenericForeignKey('content_type', 'object_id')
obj = DegreeCourse.objects.filter(title='python全栈').first()
PricePolicy.objects.create(price=9.9, period=30, content_object=obj)
'''