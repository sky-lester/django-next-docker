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
    
    if request.method == 'POST':
        data = request.data
        print(f"Request data: {data}")  # Debug print
        serializer = HelloSerializer(data=data)
        if not serializer.is_valid():
            print(f"Validation errors: {serializer.errors}")  # Debug print
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
