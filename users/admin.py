from django.contrib import admin

from users.models import User, Pet, Animal, PetContainer

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Animal)
admin.site.register(PetContainer)