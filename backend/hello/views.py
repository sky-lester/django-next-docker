from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hello
from .serializers import HelloSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World! API Django!</h1>")

@api_view(['GET', 'POST'])
def hellos(request):
    if request.method == 'GET':
        hello = Hello.objects.all()
        serializer = HelloSerializer(hello, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializer = HelloSerializer(data=data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
