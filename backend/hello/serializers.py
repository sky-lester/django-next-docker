from rest_framework import serializers
from hello.models import Hello

class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hello
        fields = '__all__'