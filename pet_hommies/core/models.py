from django.db import models


class AnimalKind(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Breed(models.Model):
    animal_kind = models.ForeignKey(AnimalKind, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('animal_kind', 'name')


class Gender(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Color(models.Model):
    animal_kind = models.ForeignKey(AnimalKind, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('animal_kind', 'name')


class Wool(models.Model):
    animal_kind = models.ForeignKey(AnimalKind, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=30)

    class Meta:
        unique_together = ('animal_kind', 'type')


class Ears(models.Model):
    type = models.CharField(max_length=30, unique=True)


class Organization(models.Model):
    name = models.TextField(unique=True)


class Home(models.Model):
    address = models.TextField()
    organization = models.ForeignKey(to=Organization, on_delete=models.DO_NOTHING)
    head_name = models.TextField()
    official_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)


class Tail(models.Model):
    type = models.TextField(unique=True)


class DepartureReason(models.Model):
    reason_type = models.TextField(unique=True)


class DeathReason(models.Model):
    death_reason = models.TextField(unique=True, blank=True, null=True)


class EuthanasiaReason(models.Model):
    reason = models.TextField(unique=True)


class Animal(models.Model):
    card_id = models.CharField(max_length=8)
    age = models.DateField(null=True, blank=True)
    weight = models.IntegerField()
    nickname = models.CharField(max_length=40, null=True, blank=True)
    tips = models.TextField(blank=True, null=True)
    cell = models.IntegerField(blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, null=True, blank=True)
    wool = models.ForeignKey(Wool, on_delete=models.DO_NOTHING, null=True, blank=True)
    ears = models.ForeignKey(Ears, on_delete=models.DO_NOTHING, null=True, blank=True)
    tail = models.ForeignKey(Tail, on_delete=models.DO_NOTHING, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=40, null=True, blank=True)
    mark_id = models.CharField(max_length=40, unique=True, null=True, blank=True)
    date_sterilization = models.CharField(max_length=100, blank=True, null=True)
    socialized = models.BooleanField()
    admission_id = models.CharField(max_length=50, blank=True, null=True)
    admission_id_date = models.DateField(blank=True, null=True)
    catch_id = models.CharField(max_length=40, blank=True, null=True)
    catch_address = models.TextField(blank=True, null=True)
    legal_entity = models.TextField(blank=True, null=True)
    holder_name = models.TextField(blank=True, null=True)
    individual_entity = models.TextField(blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    admission_id_2 = models.CharField(max_length=40, null=True, blank=True)
    knock_out_date = models.DateField(blank=True, null=True)
    knock_out_reason = models.TextField(blank=True, null=True)
    knock_out_id = models.CharField(max_length=40, blank=True, null=True)
    worker_name = models.CharField(max_length=50, blank=True, null=True)
    departure_reason = models.ForeignKey(DepartureReason, on_delete=models.DO_NOTHING, blank=True, null=True)
    parasite_treatment_id = models.IntegerField(blank=True, null=True)
    parasite_treatment_date = models.DateField(blank=True, null=True)
    parasite_treatment_drug = models.CharField(max_length=50, blank=True, null=True)
    parasite_treatment_drug_dose = models.IntegerField(blank=True, null=True)
    vaccine_id = models.IntegerField(blank=True, null=True)
    vaccine_dates = models.TextField(blank=True, null=True)
    vaccine_type = models.CharField(max_length=40, blank=True, null=True)
    vaccine_series = models.IntegerField(blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    inspection_result = models.IntegerField(blank=True, null=True)
    home = models.ForeignKey(Home, on_delete=models.DO_NOTHING, blank=True, null=True)
