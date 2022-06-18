from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('student/list', views.liststudent, name='liststudent'),
    path('student/addstudent', views.addstudent, name='addstudent'),
    path('student/<pk>/edit', UpdatePostView.as_view()),
    path('student/<pk>/delete', DeletePostView.as_view()),
    path('student/export',views.export_student,name='export_student'),
    path('student/import',views.import_student,name='import_student'),

]