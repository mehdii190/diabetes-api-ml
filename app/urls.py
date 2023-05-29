
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name="home"),
    path('predict/',views.predict),
    path('predict/result/',views.result),
    path('guide/',views.guide),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path("logout/", views.logout, name="logout"),
]