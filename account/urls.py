from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import (UserLoginForm)

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
    # form_class=UserLoginForm), name='login'),
    path('register/', views.account_register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
