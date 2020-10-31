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


# class AnimalInfoView(APIView):
#     def get(self):
#         animals = Animal.objects.filter(socialized=True)
#         serializer = AnimalTypeSerializer(animals, many=True)
