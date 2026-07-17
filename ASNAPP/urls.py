from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Login, name='Login'),
    path('register/', views.Register, name='Register'),
    path('userhome/', views.userhome, name='userhome'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminac/',views.adminac, name='adminac'),
    path('add_product/<int:id>/', views.add_product, name='add_product'),
    path('add_specifications/<int:id>/', views.add_specifications, name='add_specifications'),
    path('userviewcompany/', views.userviewcompany, name='userviewcompany'),
    path('userviewmodel/<int:id>/', views.userviewmodel, name='userviewmodel'),
    path('userviewspecification/<int:id>/', views.userviewspecification, name='userviewspecification'),
    path('delete_company/<int:id>/', views.delete_company, name='delete_company'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('delete_specification/<int:id>/', views.delete_specification, name='delete_specification'),
    path('logout/', views.logout, name='logout'),
]
