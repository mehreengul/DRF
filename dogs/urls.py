from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('dogs/', views.DogList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),

    path('breed/', views.BreedList.as_view()),
    path('breed/<int:pk>/', views.BreedDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
