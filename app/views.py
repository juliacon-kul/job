from django.shortcuts import render
from app.models import Element, ElementData
from app.serializers import ElementSerializer, ElementDataSerializer
from rest_framework import generics

# Create your views here.
class ElementList(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ElementDataList(generics.ListCreateAPIView):
    queryset = ElementData.objects.all()
    serializer_class = ElementDataSerializer

class ElementDetail(generics.RetrieveAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
