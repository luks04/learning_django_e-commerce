from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__" # ['id', 'name', 'duration', 'rating']

'''
class <ClassName>Serializer(serializers.ModelSerializer):
    class Meta:
        model = <ClassName>
        fields = "__all__" # The same that a list with all the <ClassName> fields
'''
