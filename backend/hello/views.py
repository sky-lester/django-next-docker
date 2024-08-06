from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hello
from .serializers import HelloSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        hello = Hello.objects.all()
        serializer = HelloSerializer(hello, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
