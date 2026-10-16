from django.urls import path
from .views import BreedList, BreedDetail, DogList, DogDetail

urlpatterns = [
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:pk>/', BreedDetail.as_view(), name='breed-detail'),
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
]