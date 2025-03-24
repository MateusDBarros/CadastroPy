from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView


# Create your views here.

class PersonCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'pk'

class PersonList(APIView):
    def get(self, request):

        name = request.query_params.get('name', '')

        if name:
            person = Person.objects.filter(title_icontains=name)
        else:
            person = Person.objects.all()

        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)