from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create dog models here.
class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=15)
    color = models.CharField(max_length=25)
    favoriteFood = models.CharField(max_length=50)
    favoriteToy = models.CharField(max_length=25)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)

    # created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


# list
Sizes = [
    ('Tiny', 'Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large')
]


# Create breed models here.
class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    size = models.CharField(choices=Sizes, default='Medium', max_length=50)
    friendliness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])


    def __str__(self):
        return self.name
