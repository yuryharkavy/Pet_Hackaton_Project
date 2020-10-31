import pandas as pd
from core.models import *
from psycopg2.errors import UniqueViolation
from django.db.utils import IntegrityError
import datetime
from django.utils.dateparse import parse_datetime

# from pet_hommies.core.models import *


def parse_socialized(text):
    return text == 'да'


# def import_data(filename='/Users/yuranous/PycharmProjects/Pet_Hackaton_Project/pet_hommies/core/data.xlsx'):
reader = pd.read_excel('/Users/yuranous/PycharmProjects/Pet_Hackaton_Project/pet_hommies/core/data.xlsx')
for _, row in reader.iterrows():

    if _ == 0:
        continue

    try:
        gender = Gender.objects.create(name=row[6].lower())
    except (UniqueViolation, IntegrityError):
        gender = Gender.objects.get(name=row[6].lower())

    try:
        kind = AnimalKind.objects.create(name=row[2].lower())
    except (UniqueViolation, IntegrityError):
        kind = AnimalKind.objects.get(name=row[2].lower())

    try:
        breed = Breed.objects.create(animal_kind=kind, name=row[7].lower())
    except (UniqueViolation, IntegrityError):
        breed = Breed.objects.get(animal_kind=kind, name=row[7].lower())

    try:
        tail = Tail.objects.create(type=row[11].lower())
    except (UniqueViolation, IntegrityError):
        tail = Tail.objects.get(type=row[11].lower())

    try:
        color = Color.objects.create(animal_kind=kind, name=row[8].lower())
    except (UniqueViolation, IntegrityError):
        color = Color.objects.get(animal_kind=kind, name=row[8].lower())

    try:
        wool = Wool.objects.create(animal_kind=kind, type=row[9].lower())
    except (UniqueViolation, IntegrityError):
        wool = Wool.objects.get(animal_kind=kind, type=row[9].lower())

    try:
        ears = Ears.objects.create(type=row[10].lower())
    except (UniqueViolation, IntegrityError):
        ears = Ears.objects.get(type=row[10].lower())

    try:
        organization = Organization.objects.create(name=row[42].lower())
    except (UniqueViolation, IntegrityError):
        organization = Organization.objects.get(name=row[42].lower())

    try:
        home = Home.objects.create(
            address=row[41],
            organization=organization,
            head_name=row[43]
        )
    except (UniqueViolation, IntegrityError):
        home = Home.objects.get(
            address=row[41],
            organization=organization,
            head_name=row[43]
        )

    try:
        animal = Animal.objects.create(
            card_id=row[1],
            # age=str(row[3]),
            weight=row[4],
            nickname=row[5],
            gender=gender,
            breed=breed,
            color=color,
            wool=wool,
            ears=ears,
            tail=tail,
            size=row[12],
            tips=row[13],
            mark_id=row[15],
            date_sterilization=row[16],
            socialized=parse_socialized(row[18]),
            admission_id=row[19],
            admission_id_date=parse_datetime(str(row[20])),
            catch_id=row[22],
            catch_address=row[23],
            admission_date=parse_datetime(str(row[36])),
            home=home
        )
    except (UniqueViolation, IntegrityError):
        pass
    index = _

#todo:добаваить округ и врача + всяких лиц