from django.urls import path
from .views import AnimalView, AnimalInfoView
app_name = "animals"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('get_animals/', AnimalInfoView.as_view())
]