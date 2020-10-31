from django.urls import path

from .views import AnimalView, MainAnimalInfoView
from rest_framework_swagger.views import get_swagger_view

app_name = "animals"
# app_name will help us do a reverse look-up latter.
schema_view = get_swagger_view(title='Pets\' Hommies Api')

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('get_animals/', MainAnimalInfoView.as_view()),
    path('swagger/', schema_view)
]
