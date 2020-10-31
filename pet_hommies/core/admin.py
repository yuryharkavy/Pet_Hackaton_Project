from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AnimalKind)
admin.site.register(Animal)
admin.site.register(Home)
admin.site.register(Organization)
admin.site.register(Gender)
admin.site.register(Color)
admin.site.register(Wool)
admin.site.register(Ears)
admin.site.register(Tail)
admin.site.register(DeathReason)
admin.site.register(DepartureReason)
admin.site.register(EuthanasiaReason)