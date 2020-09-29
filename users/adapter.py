from allauth.account import app_settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import import_attribute
from django.db import transaction
from schedule.models import Calendar


class CustomAccountAdapter(DefaultAccountAdapter):

    @transaction.atomic
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_username, user_email, user_field

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('email')
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)

        # Create calendar during registration process
        calendar = Calendar.objects.create(name=email, slug=email)

        user.calendar = calendar
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user


def get_adapter(request=None):
    return import_attribute(app_settings.ADAPTER)(request)
