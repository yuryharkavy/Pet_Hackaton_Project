import pandas as pd
from core.models import *

from pet_hommies.core.models import *


def import_data(filename='/Users/yuranous/PycharmProjects/Pet_Hackaton_Project/pet_hommies/core/data.xlsx'):
    reader = pd.read_excel(filename)
    for _, row in reader.iterrows():

        if _ == 0:
            continue
        gender = Gender.objects.create(name=row[6])
        if gender not in Gender.objects.all():
            gender.save()

        kind = AnimalKind.objects.create(name=row[2])
        if kind not in AnimalKind.objects.all():
            kind.save()

        breed = Breed.objects.create(animal_kind=kind, name=row[7])
        if breed not in Breed.objects.all():
            breed.save()

        tail = Tail.objects.create(type=row[11])
        if tail not in Tail.objects.all():
            tail.save()

        color = Color.objects.create(animal_kind=kind, name=row[8])
        if color not in Color.objects.all():
            color.save()

        wool = Wool.objects.create(animal_kind=kind, type=row[9])
        if wool not in Color.objects.all():
            wool.save()

        ears = Ears.objects.create(type=row[10])
        if ears not in Ears.objects.all():
            ears.save()

        organization = Organization.objects.create(name=row[42])
        if organization not in Organization.objects.all():
            organization.save()

        home = Home.objects.create(
            address=row[41],
            organization=organization,
            head_name=row[43]
        )
        if home not in Home.objects.all():
            home.save()