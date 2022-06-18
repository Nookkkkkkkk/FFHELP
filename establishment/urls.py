from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('establishment/list', views.listestablishment, name='listestablishment'),
    path('establishment/addestablishment', views.addestablishment, name='addestablishment'),
    path('establishment/<pk>/edit', UpdatePostView.as_view()),  
    path('establishment/<pk>/delete', DeletePostView.as_view()),
    path('establishment/export',views.export_establishment,name='export_establishment'),
    path('establishment/import',views.import_establishment,name='import_establishment'),  
]