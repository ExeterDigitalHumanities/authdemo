"""authdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='about.html'), name='about'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='about'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('accounts/profile/', auth_views.TemplateView.as_view(template_name='registration/details.html'), name='profile'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view, name='password_change_done'),
    path('password_reset_done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view, name='password_reset_confirm'),

]
