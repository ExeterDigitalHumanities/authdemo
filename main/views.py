from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UsersOnly(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'users_only.html')


class RequireLogin(LoginRequiredMixin,View):
    raise_exception = True

    def get(self, request):
        return render(request, 'require_login.html')


