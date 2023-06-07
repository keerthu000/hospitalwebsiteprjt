from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('appoinment',views.appoinment,name='appoinment'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]