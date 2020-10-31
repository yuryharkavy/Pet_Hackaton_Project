from rest_framework import serializers

from .models import Animal


class AnimalTypeSerializer(serializers.Serializer):
    name = serializers.CharField()


class AnimalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['card_id', 'age',
                  'weight',
                  'nickname',
                  'tips',
                  'cell',
                  'tail',
                  'breed', 'gender', 'mark_id',
                  'date_sterilization',
                  'socialized',
                  'admission_id',
                  'admission_id_date',
                  'catch_id',
                  'catch_address',
                  'legal_entity',
                  'holder_name',
                  'individual_entity',
                  'admission_date',
                  'admission_id_2',
                  'knock_out_date',
                  'knock_out_reason',
                  'knock_out_id',
                  'worker_name',
                  'departure_reason',
                  'parasite_treatment_id',
                  'parasite_treatment_date',
                  'parasite_treatment_drug',
                  'parasite_treatment_drug_dose',
                  'vaccine_id',
                  'vaccine_dates',
                  'vaccine_type',
                  'vaccine_series',
                  'inspection_date',
                  'inspection_result']
