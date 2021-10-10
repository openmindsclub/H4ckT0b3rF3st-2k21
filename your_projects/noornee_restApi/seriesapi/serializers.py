from rest_framework import serializers
from .models import Series

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'duration', 'genre', 'number_of_episodes', 'rating', 'date_added']
