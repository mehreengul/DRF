from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    # breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    # breed = BreedSerializer()
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)
    breed = BreedSerializer(read_only=True)

    class Meta:
        model = Dog
        fields = '__all__'
