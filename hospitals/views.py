from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import City, Hospital
from .forms import CityForm, HospitalForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import HospitalForm

from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404, redirect, render
from .models import Hospital

from django.http import JsonResponse
# Create your views here.
def hospital(request, id):
    hospital = Hospital.objects.filter(id=id).first()
    return render(request, 'hospitals/patient.html', context={'hospitals': hospital})
    

from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

from django.views.decorators.http import require_POST
from .forms import PatientForm


@api_view(['GET', 'POST'])
def add_patient(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@login_required
def city_list(request):
    cities = City.objects.all()
    return render(request, 'hospitals/city_list.html', {'cities': cities})

@login_required
def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'city': city})


@api_view(['POST'])
@permission_classes([IsAdminUser])
def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            # Get the URL for the 'hospital_list' view
            url = reverse('city_list')
            # Redirect to the 'hospital_list' URL
            return redirect('city_list')
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm(instance=city)
    return render(request, 'hospitals/editCity.html', {'form': form, 'city': city})


@staff_member_required
def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('city_list')
    return render(request, 'city_confirm_delete.html', {'city': city})




@login_required
def hospital_list(request):
    hospitals = Hospital.objects.all()
    cities = City.objects.all()
    return render(request, 'hospitals/hospitals_lists.html', {'hospitals': hospitals, "cities":cities})

@login_required
def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'hospitals_lists.html', {'hospital': hospital})


@api_view(['POST'])
@permission_classes([IsAdminUser])
def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            hospital = form.save()
            # Get the URL for the 'hospital_list' view
            url = reverse('hospital_list')
            # Redirect to the 'hospital_list' URL
            return redirect('hospital_list')
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospital
from .forms import HospitalForm
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def hospital_update(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_detail', pk=hospital.pk)
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospitals/editHospital.html', {'form': form})


@staff_member_required
def hospital_delete(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, 'hospital_confirm_delete.html', {'hospital': hospital})

def city_list_json(request):
    cities = City.objects.all()
    data = {'cities': list(cities.values())}
    return JsonResponse(data)

def hospital_list_json(request, city):
    hospitals = Hospital.objects.filter(city__name=city)
    data = {'hospitals': list(hospitals.values())}
    return JsonResponse(data)
