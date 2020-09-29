from django.contrib import admin

from users.models import User, Pet, Animal

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Animal)
