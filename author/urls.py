from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

     path('register/', views.register, name="register"),
     # path('user_login/', views.user_login, name="user_login"),
     path('user_login/', views.UserLoginView.as_view(), name="user_login"),
     path('profile/', views.profile, name="profile"),
     # path('logout/', views.user_logout, name='logout'),
     path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),
     path('profile/edit/', views.edit_profile, name='edit_profile'),
     path('profile/pass_change/', views.pass_change, name='pass_change')

]