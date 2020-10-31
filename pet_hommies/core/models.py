from django.db import models


# Create your models here.
class Animal(models.Model):
    card_id = models.CharField(max_length=8)
    age = models.IntegerField
    weight = models.IntegerField
    nickname = models.CharField(max_length=20)
    tips = models.TextField
    cell = models.IntegerField
    mark_id = models.IntegerField(primary_key=True)
    date_sterilization = models.CharField(max_length=30)
    socialized = models.BooleanField
    admission_id = models.CharField(max_length=20, primary_key=True)
    admission_id_date = models.DateField
    catch_id = models.CharField(max_length=20)
    catch_address = models.TextField
    legal_entity = models.TextField
    holder_name = models.TextField
    individual_entity = models.TextField
    admission_date = models.DateField
    admission_id_2 = models.CharField(max_length=20, primary_key=True)
    knock_out_date = models.DateField
    knock_out_reason = models.TextField
    knock_out_id = models.CharField(primary_key=True, max_length=20)
    worker_name = models.CharField(max_length=50)
    parasite_treatment_id = models.IntegerField
    parasite_treatment_date = models.DateField
    parasite_treatment_drug = models.CharField(max_length=50)
    parasite_treatment_drug_dose = models.IntegerField
    vaccine_id = models.IntegerField
    vaccine_dates = models.TextField
    vaccine_type = models.CharField(max_length=40)
    vaccine_series = models.IntegerField
    inspection_date = models.DateField
    inspection_result = models.IntegerField

# class Breed(models.Model):
