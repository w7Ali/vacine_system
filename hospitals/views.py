from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import City, Hospital
from .forms import CityForm, HospitalForm
# Create your views here.
def hospital(request):

    pass



@login_required
def city_list(request):
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})

@login_required
def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'city': city})

@staff_member_required
def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm()
    return render(request, 'city_form.html', {'form': form})

@staff_member_required
def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'city_form.html', {'form': form})

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
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

@login_required
def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'hospital_detail.html', {'hospital': hospital})

@staff_member_required
def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            hospital = form.save()
            return redirect('hospital_detail', pk=hospital.pk)
    else:
        form = HospitalForm()
    return render(request, 'hospital_form.html', {'form': form})

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
    return render(request, 'hospital_form.html', {'form': form})

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
