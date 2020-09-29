from django import forms
from users.models import Pet


class AddPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name']

    # def __init__(self, *args, **kwargs):
    #     print('cos')
    #     self.request = kwargs.pop('request')
    #     super(AddPetForm, self).__init__()
    # def save(self):
    #     user = super(AddPetForm, self).save(request)
    #     user.save()
    #     return user