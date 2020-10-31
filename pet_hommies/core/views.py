# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AnimalKind, Animal
from .serializer import AnimalTypeSerializer


class AnimalView(APIView):
    def get(self, request):
        animal_type = AnimalKind.objects.all()
        serializer = AnimalTypeSerializer(animal_type, many=True)

        return Response({"animal types": serializer.data})

    def post(self, request):
        return Response({"animal types": request.data['hello']})


class MainAnimalInfoView(APIView):
    def get(self, request):
        animals = Animal.objects.filter(socialized=True)
        interesting_info_animals = [{"color": a.color.name, "breed": a.breed_id, "age": a.age, "weight": a.weight,
                                     "date_sterilization": a.date_sterilization, "gender_id": a.gender_id,
                                     'vaccine_date': a.vaccine_dates} for a
                                    in list(animals)]
        # serializer = AnimalInfoSerializer(interesting_info_animals, many=True)
        return Response({"animals": interesting_info_animals})
