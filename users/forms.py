from django import forms
from django.template.defaultfilters import slugify
from photologue.models import Gallery, Photo

from users.models import Pet


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
