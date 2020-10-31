from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import AnimalView, AnimalTableInfo, MainAnimalInfoView, AnimalCardView
app_name = "animals"
# app_name will help us do a reverse look-up latter.
schema_view = get_swagger_view(title='Pets\' Hommies Api')

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('get_animals/', MainAnimalInfoView.as_view()),
    path('swagger/', schema_view),
    path('card/<animal_id>/', AnimalCardView.as_view()),
    path('table/', AnimalTableInfo),
]
