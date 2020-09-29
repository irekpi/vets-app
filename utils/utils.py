from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from users.models import User


class LoginAccessMixin(LoginRequiredMixin):
    login_url = reverse_lazy('account_login')


class BaseContextMixinView:
    """Groups of users that are allowed to view specific parts of sites """

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name=User.DOCTOR):
            context['user_type'] = User.DOCTOR
        if self.request.user.groups.filter(name=User.PATIENT):
            context['user_type'] = User.PATIENT
        return context
