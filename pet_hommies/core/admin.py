from django.contrib import admin

# Register your models here.
from .models import AnimalKind

admin.site.register(AnimalKind)