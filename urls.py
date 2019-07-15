from django.conf.urls import url
from django.contrib import admin
from volt import views
from tech import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^index',views.index,name='index'),
    url(r'^studentlogin/',views.student_login,name='studentlogin'),
    url(r'^student_signup/',views.student_signup,name='studentsignup'),
    url(r'^login/',views.employees,name='employees'),
    url(r'^adminlogin/',views.admin,name='admin'),
    url(r'^createnewaccount/',views.jobseeker,name='jobseeker'),
    url(r'^forgetpassword/',views.forgetpassword,name='forgetpassword'),
    url(r'^exammainpage/',views.exammainpage,name='exammainpage'),
    url(r'^javaexam/',views.javaexam,name='javaexam'),
    url(r'^pythonexam/',views.pythonexam,name='pythonexam'),
    url(r'^phpexam/',views.phpexam,name='phpexam'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^applynow/',views.applynow,name='applynow'),
    url(r'^freshersignup/',views.fresher_signup,name='freshersignup'),
    url(r'^phpbasictest/',views.phpbasictest,name='phpbasictest'),
    url(r'^phpmocktest/',views.phpmocktest,name='phpmocktest'),
    url(r'^pythonbasictest/',views.pythonbasictest,name='pythonbasictest'),
    url(r'^pythonmocktest/',views.pythonmocktest,name='pythonmocktest'),
    url(r'^javabasictest/',views.java_basictest),
    url(r'^javamocktest/',views.javamocktest,name='javamocktest'),
    url(r'^hrmanagerlogin/',views.hrmanagerlogin,name='hrmanagerlogin'),
    url(r'^technicalmanagerlogin/',views.technicalmanagerlogin,name='technicalmanagerlogin'),
    url(r'^hrpage/',views.hrpage,name='hrpage'),
    url(r'^teamleaderpage/',views.teamleaderpage,name='teamleaderpage'),
    url(r'^technicalmanagerpage/',views.technicalmanagerpage,name='technicalmanagerpage'),
    url(r'^teamleaderlogin/',views.teamleaderlogin,name='teamleaderlogin'),
    url(r'^experiencesignup/',views.experiencesignup,name='experiencesignup'),
    url(r'^fresherlogin/',views.fresherlogin,name='fresherlogin'),
    url(r'^experiencelogin/',views.experiencelogin,name='experiencelogin'),
    url(r'^admin1/',views.admin1,name='admin1'),
    url(r'^addemployee/',views.ademp,name='addemployee'),
    url(r'^viewemployee/',views.viewemp,name='viewemployee'),
    url(r'^addstudent/',views.addstu,name='addstudent'),
    url(r'^viewstudent/',views.viewstu,name='viewstudent'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#     urlpatterns += patterns('',
#     	url(r'\^media/(?P<path>.\*)\$', 'django.views.static.serve',
#     		{'document_root': settings.MEDIA_ROOT, }),
# )


