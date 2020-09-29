from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import gettext_lazy as _

PATIENT = 'patient'
DOCTOR = 'doctor'

GROUPS_NAME = {
    PATIENT: _('Pacjent'),
    DOCTOR: _('Doktor')
}


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group
    try:
        Group.objects.create(name=GROUPS_NAME.get(PATIENT))
        Group.objects.create(name=GROUPS_NAME.get(DOCTOR))
    except:  # TODO add error
        pass


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        post_migrate.connect(create_groups)
