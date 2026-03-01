from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('android' , views.android , name = 'android'),
    path('contact' , views.contact , name = 'contact'),
    path('course_details/<int:course_id>/' , views.course_details , name = 'course_details'),
    path('cyber1' , views.cyber1 , name = 'cyber1'),
    path('cyber2' , views.cyber2 , name = 'cyber2'),
    path('flutter' , views.course_details , name = 'flutter'),
    path('' , views.index , name = 'home'),
    path('java' , views.java , name = 'java'),
    path('login' , views.loginpage , name = 'login'),
    path('logout' , views.logoutuser , name = 'logout'),
    path('profile' , views.profile , name = 'profile'),
    path('reg' , views.reg , name = 'reg'),
    path('web1' , views.web1 , name = 'web1'),
    path ('base' , views.base , name = 'base'),
    path('add_course' , views.add_course, name = 'add_course'),
    path('delete_course/<int:course_id>/' , views.delete_course, name = 'delete_course'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)