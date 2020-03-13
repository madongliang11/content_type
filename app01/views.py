from django.shortcuts import render, HttpResponse

from app01.models import DegreeCourse, PricePolicy, Course

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


def test(request):
    # 1、为学位课“python全栈”添加一个价格策略：一个月 9.9
    # obj1 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=9.9, period=30, content_object=obj1)
    #
    # obj2 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=19.9, period=60, content_object=obj2)
    #
    # obj3 = DegreeCourse.objects.filter(title='python全栈').first()
    # PricePolicy.objects.create(price=29.9, period=90, content_object=obj3)

    # 2、为普通课“rest framework”添加一个价格策略：一个月 10
    # obj1 = Course.objects.filter(title='rest framework').first()
    # PricePolicy.objects.create(price=10, period=30, content_object=obj1)
    #
    # obj2 = Course.objects.filter(title='rest framework').first()
    # PricePolicy.objects.create(price=20, period=60, content_object=obj2)
    #
    # obj3 = Course.objects.filter(title='rest framework').first()
    # PricePolicy.objects.create(price=30, period=90, content_object=obj3)

    # 3、根据课程id获取课程，并获取该课程所有的价格策略
    course = Course.objects.filter(id=1).first()
    price_policys = course.price_policy_list.all()
    print(price_policys)

    return HttpResponse('添加价格策略')


