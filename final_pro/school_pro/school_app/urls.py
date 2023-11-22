
from django.urls import path

from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('login2/',views.login2,name='login2'),
    path('login3/',views.login3,name='login3'),
    path('register/', views.register, name='register'),

]
