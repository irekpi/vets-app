from django.db import models
from django.utils.translation import gettext as _
from photologue.models import Gallery
from users.models import User


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
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='pet_container',
        verbose_name=_('Imie Doktora')
    )

    class Meta:
        verbose_name = _('Pupil')
        verbose_name_plural = _('Pupile')

    def __str__(self):
        return '{} {}'.format(self.owner_name, self.name)
