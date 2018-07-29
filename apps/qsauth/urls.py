from django.urls import path
from . import views

app_name = 'qsauth'

urlpatterns = [
    path("login/",views.LoginView.as_view(),name='login'),
    path("logout/",views.logout_view,name='logout'),
]