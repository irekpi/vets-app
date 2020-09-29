from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from photologue.models import Gallery
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

    class Meta:
        verbose_name = _('Użytkownik')
        verbose_name_plural = _('Użytkownicy')

    def __str__(self):
        return self.email

    @property
    def user_type_name(self):
        return dict(self.USER_TYPES).get(self.groups.first().name)


class Animal(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zwierzę'
        verbose_name_plural = "Zwierzęta"


class Pet(models.Model):
    owner_name = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name='owner_name',
        verbose_name=_('Imię właściciela')
    )
    name = models.CharField(max_length=100, null=True, verbose_name=_('Imię'))
    type = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True, blank=True, related_name='animal',
        verbose_name=_('Rodzaj zwierzęcia')
    )
    gallery = models.OneToOneField(
        Gallery, blank=True, on_delete=models.CASCADE, null=True, verbose_name=_('Galeria')
    )

    class Meta:
        verbose_name = _('Pupil')
        verbose_name_plural = _('Pupile')

    def __str__(self):
        return '{} {}'.format(self.owner_name, self.name)
