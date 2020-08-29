from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MovieEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        extra_kwargs = {
            'title': {'read_only': True},
            'description': {'read_only': True},
            'image': {'read_only': True},
        }



