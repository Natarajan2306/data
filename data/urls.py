from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('Register/', views.registerpage, name='Register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    
   ]