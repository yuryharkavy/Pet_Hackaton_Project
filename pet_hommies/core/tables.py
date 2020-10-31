import django_tables2 as tables
from .models import AnimalKind

class randomTable(tables.Table):
    class Meta:
        model = AnimalKind
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}