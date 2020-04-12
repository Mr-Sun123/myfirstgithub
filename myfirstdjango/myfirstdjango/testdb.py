# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.contrib import messages
from django.forms.models import model_to_dict
from TestModel.models import Test,Student,Teacher,Course,SC,TC
 
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

from django.shortcuts import render
from django.views.decorators import csrf
import json
from django.http import JsonResponse
def home_page1(request,param1):
    ctx={}
   
    if param1!='':
        response3 = Student.objects.get(sno=param1)
        ctx['rlt'] = model_to_dict(response3)
        ctx['rlt'].pop('id')
        ctx['rlt'].pop('spassward')
        ctx['x']='my'
    return render(request, "home_page.html", ctx)
def home_page(request,param1):
    ctx={}
    
    if request.method == 'POST':
        response3 = Student.objects.get(sno=request.POST.get('sno'))
        
        ctx['rlt'] = model_to_dict(response3)
        ctx['rlt'].pop('id')
        ctx['rlt'].pop('spassward')
    return render(request, "home_page.html", ctx)

def teacher_page(request,param1):
    ctx={}
    
    if request.method == 'POST':
        response3 = Teacher.objects.get(tno=request.POST.get('tno'))
        
        ctx['rlt'] = model_to_dict(response3)
        ctx['rlt'].pop('id')
        ctx['rlt'].pop('tpassward')
    return render(request, "teacher_page.html", ctx)

def teacher_scoring(request,param1):
    ctx={}
    ctx['rlt']={}
    response3 = Teacher.objects.get(tno=param1)
    mylist1=response3.tc_set.all()
    cnolist=[]
    for i in mylist1:
        cnolist.append(i.cno.cno)
    for i in range(len(cnolist)):
        
        ctx['rlt'][i]= model_to_dict(Course.objects.get(cno=cnolist[i]))
        ctx['rlt'][i].pop('id')
        
    ctx['rlt']['tno']=param1
    return render(request, "teacher_scoring.html", ctx)

def analys(request,param1,param2):
    ctx={}
    ctx['rlt']={}
    response3 = Course.objects.get(cname=param2)
    mylist=response3.sc_set.all()
    grade=[]
    for i in mylist:
        grade.append(i.grade)
    
    a=[0,0,0,0,0,0,0,0,0,0]
    for k in grade:
        a[int(k/10)]+=1
    ctx['rlt']['grade']=a
    ctx['rlt']['tno']=param1
    ctx['cname']=param2
    return render(request, "tu.html", ctx)

def teacher_page1(request,param1):
    ctx={}
   
    if param1!='':
        response3 = Teacher.objects.get(tno=param1)
        ctx['rlt'] = model_to_dict(response3)
        ctx['rlt'].pop('id')
        ctx['rlt'].pop('tpassward')
        ctx['x']='my'
    return render(request, "teacher_page.html", ctx)

def scoring(request,param1,param2):
    ctx={}
    ctx['rlt']={}
    course1 = Course.objects.get(cno=param2)
    mylist=course1.sc_set.all()
    
    snolist=[]
    grade=[]
    name=[]
    for i in mylist:
        snolist.append(i.sno.sno)
        name.append(i.sno.sname)
        grade.append(i.grade)
    for i in range(len(snolist)):
        ctx['rlt'][i]= dict()
        ctx['rlt'][i]['sno']=snolist[i]
        ctx['rlt'][i]['sname']=name[i]
        ctx['rlt'][i]['grade']=grade[i]
    ctx['rlt']['tno']=param1
    ctx['cname']=course1.cname
    return render(request, "scoring.html", ctx)

def ensure1(request):
    ctx={}
    ctx['rlt']={}
    student=Student.objects.get(sno=request.POST['sno'])
    course=Course.objects.get(cno=request.POST['cno'])
    sc=SC.objects.get(sno=student,cno=course)
    sc.grade=request.POST['grade']
    ctx['rlt']['tno']=request.POST['tno']
    sc.save()
    messages.success(request, "修改成功！")
    ctx['rlt']['sno']=student.sno
    ctx['rlt']['sname']=student.sname
    ctx['rlt']['cname']=course.cname
    ctx['rlt']['cno']=course.cno
    return HttpResponse("修改成功！")

def change1(request):
    ctx ={}
    ctx['rlt']={}
    ctx['rlt']['sno']=request.POST['sno']
    ctx['rlt']['tno']=request.POST['tno']
    ctx['rlt']['cname']=request.POST['cname']
    return render(request, "chage.html", ctx)

def change(request,param1,param2,param3):
    ctx={}
    ctx['rlt']={}
    student1 = Student.objects.get(sno=param1)
    ctx['rlt']['sno']=student1.sno
    ctx['rlt']['sname']=student1.sname
    ctx['rlt']['cname']=param2
    course1=Course.objects.get(cname=param2)
    ctx['rlt']['cno']=course1.cno
    ctx['rlt']['tno']=param3
    sc1=SC.objects.get(sno=student1,cno=course1)
    ctx['rlt']['grade']=sc1.grade
    return render(request, "change.html", ctx)


def selection(request,param1,param2):
    ctx={}
    
    
    response3 = Course.objects.get(cno=param2)
        
    ctx['rlt'] = model_to_dict(response3)
    ctx['rlt'].pop('id')
    ctx['rlt']['sno']=param1
    return render(request, "selection.html", ctx)
    
def ensure(request,param1,param2):
    ctx={}
    student1 = Student.objects.get(sno=param1)
    course1=Course.objects.get(cno=param2)
    
    SC1=SC(sno=student1,cno=course1,grade=0)
    SC1.save()
    ctx['rlt']={}
    ctx['rlt']['sno']=param1
    return render(request, "home_page.html", ctx)

def home_page2(request,param1):
    ctx={}
    
    if param1!='':
        ctx['rlt']={}
        response3 = Student.objects.get(sno=param1)
        mylist1=response3.sc_set.all()
        cnolist=[]
        for i in mylist1:
            cnolist.append(i.cno.cno)
        mylist = Course.objects.all()
        for i in range(len(mylist)):
            if mylist[i].cno not in cnolist:
                
                ctx['rlt'][i]= model_to_dict(mylist[i])
                ctx['rlt'][i].pop('id')
        ctx['rlt']['sno']=param1
        
    return render(request, "course_selection.html", ctx)

def home_page3(request,param1):
    ctx={}  
    ctx['rlt']={}
    response3 = Student.objects.get(sno=param1)
    mylist=response3.sc_set.all()
    cnolist=[]
    grade=[]
    for i in mylist:
        cnolist.append(i.cno.cno)
        grade.append(i.grade)
    for i in range(len(cnolist)):
        response4 = Course.objects.get(cno=cnolist[i])
        ctx['rlt'][i]= model_to_dict(response4)
        ctx['rlt'][i]['grade']=grade[i]
        ctx['rlt'][i].pop('id')
        
    ctx['rlt']['sno']=param1
        
    return render(request, "already_selection.html", ctx)

# 接收POST请求数据
def login(request):
    ctx ={}
    ctx['rlt']={}
    if request.POST:
        if request.POST['id']=='student':
            response2 = Student.objects.filter(sno=request.POST['myno'],spassward=request.POST['mypassward'])
            if response2:
                response3 = Student.objects.get(sno=request.POST['myno'])
                
                ctx['rlt'] = model_to_dict(response3)
                ctx['rlt'].pop('id')
                ctx['rlt'].pop('spassward')
                ctx['x']=ctx['rlt']['sno']
                return render(request, "home_page.html", ctx)
            else:
                ctx['rlt']="账户或密码不正确！"
                messages.success(request, "账户或密码不正确！")
        else:
            response2 = Teacher.objects.filter(tno=request.POST['myno'],tpassward=request.POST['mypassward'])
            if response2:
                response3 = Teacher.objects.get(tno=request.POST['myno'])
                ctx['rlt'] = model_to_dict(response3)
                ctx['rlt'].pop('id')
                ctx['rlt'].pop('tpassward')
                ctx['x']=ctx['rlt']['tno']
                return render(request, "teacher_page.html", ctx)
                
            else:
                ctx['rlt']="账户或密码不正确！"
                messages.success(request, "账户或密码不正确！")
    return render(request, "login.html", ctx)


# 接收POST请求数据
def post_student(request):
    ctx ={}
    if request.POST:
        response2 = Student.objects.filter(sno=request.POST['sno'])
        if not response2:
            student1=Student(sno=request.POST['sno'],sname=request.POST['sname'],spassward=request.POST['spassward'],sage=request.POST['sage'],ssex=request.POST['ssex'],sdept=request.POST['sdept'],swhere=request.POST['swhere'])
            student1.save()
            ctx['rlt'] = "成功！"
            messages.success(request, "成功！")
            return render(request, "login.html", ctx)
        else:
            ctx['rlt']="此用户已存在"
            messages.success(request, "此用户已存在！")
            return render(request, "registerStudent.html", ctx)
    return render(request, "registerStudent.html", ctx)

# 接收POST请求数据
def post_teacher(request):
    ctx ={}
    if request.POST:
        response2 = Teacher.objects.filter(tno=request.POST['tno'])
        if not response2:
            teacher1=Teacher(tno=request.POST['tno'],tname=request.POST['tname'],tpassward=request.POST['tpassward'],tage=request.POST['tage'],tsex=request.POST['tsex'],tdept=request.POST['tdept'],trank=request.POST['trank'])
            teacher1.save()
            ctx['rlt'] = "成功！"
            messages.success(request, "成功！")
        else:
            ctx['rlt']="此用户已存在"
            messages.success(request, "此用户已存在！")
    return render(request, "registerTeacher.html", ctx)

# 获取数据
def inqure(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

#更新数据
def updata(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")
# 删除数据
def delete(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")