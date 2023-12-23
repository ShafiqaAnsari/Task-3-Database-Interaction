from django.shortcuts import render
from .models import book2
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#this will list all the books and we can also add one
class books_list_create(ListCreateAPIView):
    queryset = book2.objects.all()
    serializer_class = BookSerializer

#Retrieve, Update and delete 
class books_RUD(RetrieveUpdateDestroyAPIView):
    queryset = book2.objects.all()
    serializer_class = BookSerializer
