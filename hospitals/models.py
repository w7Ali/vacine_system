from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    TYPE_CHOICES = (
        ('Government', 'Government'),
        ('Private', 'Private'),
    )
    name = models.CharField(max_length=100)
    hospital_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    beds_available = models.IntegerField()
    doctors = models.TextField()
    oxygen_cylinders = models.IntegerField()
    ventilators = models.IntegerField()
    nurses_available = models.IntegerField()
    ambulances = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact_number = models.IntegerField()
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name