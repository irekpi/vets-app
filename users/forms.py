from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users.models import User


class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPES, widget=forms.Select(), label=_('Typ konta'))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.groups.add(Group.objects.get(name=self.cleaned_data['user_type']))
        return user
