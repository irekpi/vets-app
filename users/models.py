from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from schedule.models import Calendar


class User(AbstractUser):
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    USER_TYPES = (
        (DOCTOR, 'Doktor'),
        (PATIENT, 'Pacjent'),
    )
    calendar = models.OneToOneField(Calendar, on_delete=models.CASCADE, verbose_name=_("Kalendarz"), null=True,
                                    blank=True)
    pupils = models.ForeignKey('PetContainer', on_delete=models.CASCADE, verbose_name=_("Doktor"),
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = _('Użytkownik')
        verbose_name_plural = _('Użytkownicy')

    def __str__(self):
        return self.email

    @property
    def user_type_name(self):
        return dict(self.USER_TYPES).get(self.groups.first().name)


class PetContainer(models.Model):
    doctor = models.ForeignKey(
        'User', on_delete=models.CASCADE, blank=True, related_name='doctor_name',
        verbose_name=_('Doktor')
    )

    class Meta:
        verbose_name = _('Podopieczny')
        verbose_name_plural = _('Podopieczni')

    def __str__(self):
        return '{} {}'.format(self.doctor.first_name, self.doctor.last_name)
