from django.db import models
from django.utils.translation import gettext as _


class Animal(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zwierzę'
        verbose_name_plural = "Zwierzęta"
