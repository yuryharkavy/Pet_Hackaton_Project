from django.contrib import admin

# Register your models here.
from .models import AnimalKind, Animal

admin.site.register(AnimalKind)
admin.site.register(Animal)