from django.conf.urls import url
from django.contrib import admin
from . import view,testdb,search,search2,post
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main$', view.mymain),
    url(r'^home_page$', testdb.home_page,name='home_page'),
    url(r'^teacher_page$', testdb.teacher_page,name='teacher_page'),
    
    url(r'^teacher_page/(\w+)$', testdb.teacher_page1,name='teacher_page'),
    url(r'^home_page/(\w+)$', testdb.home_page1,name='home_page'),
    url(r'^teacher_scoring/(\w+)$', testdb.teacher_scoring,name='teacher_scoring'),
    url(r'^course_selection/(\w+)$', testdb.home_page2,name='course_selection'),
    url(r'^already_selection/(\w+)$', testdb.home_page3,name='already_selection'),
    url(r'^testdb$', testdb.testdb),
    url(r'^selection/param1(\w+)param2(.+)/$', testdb.selection,name='selection'),
    url(r'^scoring/param1(\w+)param2(.+)/$', testdb.scoring,name='scoring'),
    url(r'^change/param1(\w+)param2(.+)param3(\w+)/$', testdb.change,name='change'),
    url(r'^change$', testdb.change1,name='change1'),
    url(r'^ensure1$', testdb.ensure1,name='ensure1'),
    url(r'^ensure/param1(\w+)param2(.+)/$', testdb.ensure,name='ensure'),
    url(r'^analys/param1(\w+)param2(.+)/$', testdb.analys,name='analys'),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^sno-iput$', testdb.post_student,name='sno'),
    url(r'^tno-iput$', testdb.post_teacher,name='tno'),
    url(r'^my-login$', testdb.login,name='login'),
    
]