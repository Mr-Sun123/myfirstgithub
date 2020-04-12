# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    
class Student(models.Model):
    sno    = models.CharField(max_length=10)
    sname   = models.CharField(max_length=10)
    sage    = models.IntegerField(default=0)
    spassward=models.CharField(max_length=20)
    ssex=models.CharField(max_length=10)
    sdept = models.CharField(max_length=10)
    swhere  = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    tno    = models.CharField(max_length=10)
    tname   = models.CharField(max_length=10)
    tage    = models.IntegerField(default=0)
    tpassward=models.CharField(max_length=20)
    tsex=models.CharField(max_length=10)
    tdept = models.CharField(max_length=10)
    trank  = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Course(models.Model):
    cno    = models.CharField(max_length=10)
    cname   = models.CharField(max_length=20)
    ccredit=models.IntegerField(default=0)
    
class TC(models.Model):
    cno    = models.ForeignKey(Course, on_delete=models.CASCADE,)
    tno   = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
    '''classno=   models.CharField(max_length=10)'''
    def __unicode__(self):
        return self.name
    
class SC(models.Model):
    cno    = models.ForeignKey(Course, on_delete=models.CASCADE,)
    sno   = models.ForeignKey(Student, on_delete=models.CASCADE,)
    '''classno=models.ForeignKey(TC, on_delete=models.CASCADE,)'''
    grade=models.IntegerField(default=0)



'''   
class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
'''