# Create your views here.
import os

from django.http import HttpResponseNotFound, FileResponse
from docxtpl import DocxTemplate
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


class AnimalCardView(View):
    def get(self, request, animal_id):
        animal = Animal.objects.get(id=int(animal_id))
        doc = DocxTemplate('/Users/yuranous/PycharmProjects/Pet_Hackaton_Project/pet_hommies/core/templates/animal_card.docx')
        context = {
            'card_id': animal.card_id,
            'address': animal.home.address,
            'organization': animal.home.organization
        }
        doc.render(context)
        doc.save('temp.doc')

        try:
            with open('temp.doc', 'rb') as f:
                response = FileResponse(f.read(), filename='карточка.docx', as_attachment=True)
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound('<h1>File not exist</h1>')
        os.remove('temp.doc')
        return response


class MainAnimalInfoView(APIView):
    def get(self, request):
        animals = Animal.objects.filter(socialized=True)
        interesting_info_animals = [{"color": a.color.name, "breed": a.breed_id, "age": a.age, "weight": a.weight,
                                     "date_sterilization": a.date_sterilization, "gender_id": a.gender_id,
                                     'vaccine_date': a.vaccine_dates} for a
                                    in list(animals)]
        # serializer = AnimalInfoSerializer(interesting_info_animals, many=True)
        return Response({"animals": interesting_info_animals})


def AnimalTableInfo(request):
    return render(request, 'people.html', {'people': AnimalKind.objects.all()})
