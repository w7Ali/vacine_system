"""VaccineManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vaccine.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('vaccineHistory', vaccineHistory, name='vaccineHistory'),
    path('new_Vaccine', new_Vaccine, name='new_Vaccine'),
    path('viewHistory/<int:pid>', viewHistory, name='viewHistory'),

    path('alreadyReg_Vaccine', alreadyReg_Vaccine, name='alreadyReg_Vaccine'),
    path('individual', individual, name='individual'),
    path('viewIndividualDtls/<int:pid>', viewIndividualDtls, name='viewIndividualDtls'),
    path('deleteIndividual/<int:pid>', deleteIndividual, name='deleteIndividual'),


    path('vaccine', vaccine, name='vaccine'),
    path('editVaccine/<int:pid>', editVaccine, name='editVaccine'),
    path('deleteVaccine/<int:pid>', deleteVaccine, name='deleteVaccine'),

    path('vaccineArea', vaccineArea, name='vaccineArea'),
    path('editVaccineArea/<int:pid>', editVaccineArea, name='editVaccineArea'),
    path('deleteVaccineArea/<int:pid>', deleteVaccineArea, name='deleteVaccineArea'),

    path('userList', userList, name='userList'),
    path('editUserList/<int:pid>', editUserList, name='editUserList'),
    path('deleteUserList/<int:pid>', deleteUserList, name='deleteUserList'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),

    path('staff_login', staff_login, name='staff_login'),
    path('sdashboard', sdashboard, name='sdashboard'),
    path('staffProfile', staffProfile, name='staffProfile'),
    path('staffvaccineHistory', staffvaccineHistory, name='staffvaccineHistory'),
    path('staffnew_Vaccine', staffnew_Vaccine, name='staffnew_Vaccine'),
    path('staffviewHistory/<int:pid>', staffviewHistory, name='staffviewHistory'),

    path('staffalreadyReg_Vaccine', staffalreadyReg_Vaccine, name='staffalreadyReg_Vaccine'),
    path('staffindividual', staffindividual, name='staffindividual'),
    path('staffviewIndividualDtls/<int:pid>', staffviewIndividualDtls, name='staffviewIndividualDtls'),
    path('deletestaffIndividual/<int:pid>', deletestaffIndividual, name='deletestaffIndividual'),
    path('staffchangePassword', staffchangePassword, name='staffchangePassword'),

    path('hospitals/', include('hospitals.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
