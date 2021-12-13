from django.shortcuts import render
from rest_framework import generics
from .serializers import CarSerialzer
from .models import Car
from .permissions import IsAuthenticatedOrReadOnly


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.filter(post = True)
    serializer_class = CarSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)


