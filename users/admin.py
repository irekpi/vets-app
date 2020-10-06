from django.contrib import admin

from users.models import User, PetContainer

admin.site.register(User)
admin.site.register(PetContainer)