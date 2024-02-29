from django.urls import path,include
from . import views


urlpatterns = [
        path('', views.navbar,name='navbar'),
        path('login/', views.login,name='login'),
        path('registration/', views.registration,name='registration'),
        path('admin_login/', views.admin_login,name='admin_login'),
        path('admin_registration/', views.admin_registration,name='admin_registration'),
        path('about/', views.about,name='about'),
        path('contact/', views.contact,name='contact'),
        path('logout/', views.logout,name='logout'),
        path('admin_logout/', views.admin_logout,name='admin_logout'),
        path('userhome/', views.userhome,name='userhome'),
        path('admin_home/', views.admin_home,name='admin_home'),


]
