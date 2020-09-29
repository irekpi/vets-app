from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from photologue.models import Gallery, Photo

from users.models import Pet, User


class AddPetForm(forms.ModelForm):
    img_field = forms.ImageField(label='zdjecie')

    class Meta:
        model = Pet
        fields = ['name', 'type']

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


class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPES, widget=forms.Select(), label=_('Typ konta'))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.groups.add(Group.objects.get(name=self.cleaned_data['user_type']))
        return user
