from django.contrib import admin
from TestModel.models import Test,Student,Teacher,Course,SC,TC
 
# Register your models here.
admin.site.register([Test, Student, Teacher,Course,SC,TC])