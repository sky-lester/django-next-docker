from rest_framework import serializers
from hello.models import *

class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model: Hello
        fields: '__all__'