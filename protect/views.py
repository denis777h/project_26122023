from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BaseRegisterForm
from .models import BaseUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')




class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/default.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['is_not_premium'] = not self.request.user.groups.filter(name = 'premium').exists()
        return context


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
