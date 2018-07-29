
from django.urls import include,path
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
]