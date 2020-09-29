from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from animals.models import Animal


class User(AbstractUser):
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    USER_TYPES = (
        (DOCTOR, 'Doktor'),
        (PATIENT, 'Pacjent'),
    )
    pass

    class Meta:
        verbose_name = _('Użytkownik')
        verbose_name_plural = _('Użytkownicy')

    def __str__(self):
        return self.email

    @property
    def user_type_name(self):
        return dict(self.USER_TYPES).get(self.groups.first().name)


class Pet(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name=_('owner_name'))
    name = models.CharField(max_length=100, null=True, verbose_name=_('Imię'))
    type = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True, related_name=_('animal'))

    class Meta:
        verbose_name = _('Pupil')
        verbose_name_plural = _('Pupile')

    def __str__(self):
        return '{} {}'.format(self.owner_name, self.name)
