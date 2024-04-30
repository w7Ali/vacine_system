from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class VaccineList(models.Model):
    Name = models.CharField(max_length=250, null=True)
    Status = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class VaccineLocationList(models.Model):
    Location = models.CharField(max_length=250, null=True)
    Status = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Location

class IndividualList(models.Model):
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
    TrackingCode = models.CharField(max_length=50, null=True)
    Gender = models.CharField(max_length=20, null=True)
    DOB = models.DateField(null=True)
    Contact = models.CharField(max_length=15, null=True)
    Address = models.CharField(max_length=200, null=True)
    Status = models.CharField(max_length=50, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.FirstName

class MemberList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.FileField(max_length=50, null=True)
    Role = models.CharField(max_length=20, null=True)
    location = models.ForeignKey(VaccineLocationList, on_delete=models.CASCADE, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name

class VaccineHistoryList(models.Model):
    members = models.ForeignKey(MemberList, on_delete=models.CASCADE)
    individuals = models.ForeignKey(IndividualList, on_delete=models.CASCADE)
    vaccines = models.ForeignKey(VaccineList, on_delete=models.CASCADE)
    vaccinelocations = models.ForeignKey(VaccineLocationList, on_delete=models.CASCADE)
    VaccinationType = models.CharField(max_length=50, null=True)
    VaccinatedBy = models.CharField(max_length=250, null=True)
    Remark = models.CharField(max_length=350, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.VaccinationType

