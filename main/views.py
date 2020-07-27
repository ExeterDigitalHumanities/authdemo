from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class UsersOnly(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'users_only.html')


class RequireLogin(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        return render(request, 'require_login.html')


class RequireStaff(UserPassesTestMixin, View):
    login_url = '/login/'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        return render(request, 'require_staff.html')