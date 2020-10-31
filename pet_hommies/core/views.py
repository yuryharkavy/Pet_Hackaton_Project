# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AnimalKind
from .serializer import AnimalSerializer


class AnimalView(APIView):
    def get(self, request):
        articles = AnimalKind.objects.all()
        serializer = AnimalSerializer(articles, many=True)
        return Response({"animal types": serializer.data})

    def post(self, request):
        return Response({"animal types": request.data['hello']})

