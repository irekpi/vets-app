from django import forms
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from photologue.models import Gallery, Photo

from animals.models import Pet
from users.models import User


class AddPetForm(forms.ModelForm):
    img_field = forms.ImageField(label=_('Zdjecie'))
    doctor = forms.ModelChoiceField(User.objects.filter(groups__name=User.DOCTOR), label=_('Doktor'))

    class Meta:
        model = Pet
        fields = ['name', 'type', 'doctor']

    def save(self, commit=True):
        user = super(AddPetForm, self).save(commit=False)
        gallery_create = Gallery.objects.create(title=slugify(self.instance.name), slug=slugify(self.instance.name))
        user.gallery = gallery_create
        img_field = self.cleaned_data['img_field']
        photo = Photo.objects.create(
            image=img_field,
            title=slugify(img_field.name),
            slug=slugify(img_field.name),
        )
        gallery_create.photos.add(photo)
        user.save()
        return user
