from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from .service import PersonService


# Create your views here.
class PersonListCreateView(APIView):

    def get(self, reqiest):
        persons = PersonService.getAll()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            person = PersonService.createPerson(
                name = request.data.get('name'),
                email = request.data.get('email'),
                content = request.data.get('content')
            )
            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


