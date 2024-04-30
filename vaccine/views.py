import random

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def index(request):
    return render(request, 'index.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalvlist = VaccineList.objects.all().count()
    totalvcenter = VaccineLocationList.objects.all().count()
    totalfulvacc = IndividualList.objects.filter(Status='Fully Vaccinated').count()
    return render(request, 'dashboard.html', locals())


def new_Vaccine(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vaccine = VaccineList.objects.filter(Status='Active')
    vlocation = VaccineLocationList.objects.filter(Status='Active')

    user = request.user
    memberid = MemberList.objects.get(user=user)

    if request.method == "POST":

        vacid = request.POST['vaccines']
        vaccineid = VaccineList.objects.get(id=vacid)

        vlocid = request.POST['vaccinelocations']
        vlocationid = VaccineLocationList.objects.get(id=vlocid)

        trackno = str(random.randint(100000000000000, 999999999999999))
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        gender = request.POST['Gender']
        dob = request.POST['DOB']
        contact = request.POST['Contact']
        address = request.POST['Address']
        vactype = request.POST['VaccinationType']
        vacby = request.POST['VaccinatedBy']
        remark = request.POST['Remark']
        status = request.POST['Status']

        try:
            individual = IndividualList.objects.create(FirstName=fname, LastName=lname, TrackingCode=trackno,
                                                       Gender=gender, DOB=dob, Contact=contact, Address=address,
                                                       Status=status)
            VaccineHistoryList.objects.create(members=memberid, individuals=individual, vaccines=vaccineid,
                                              vaccinelocations=vlocationid, VaccinationType=vactype, VaccinatedBy=vacby,
                                              Remark=remark)
            error = "no"
        except:
            error = "yes"
    return render(request, 'new_Vaccine.html', locals())


def vaccineHistory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vachistory = VaccineHistoryList.objects.all().order_by('CreationDate').reverse()
    return render(request, 'vaccineHistory.html', locals())


def viewHistory(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vhistory = VaccineHistoryList.objects.get(id=pid)
    return render(request, 'viewHistory.html', locals())

def alreadyReg_Vaccine(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vaccine = VaccineList.objects.filter(Status='Active')
    vlocation = VaccineLocationList.objects.filter(Status='Active')
    indlist = None
    sd = None
    user = request.user
    memberid = MemberList.objects.get(user=user)

    try:
        if request.method == "POST":
            sd = request.POST['searchdata']
            indlist = IndividualList.objects.get(Q(TrackingCode=sd))
    except:
        if request.method == "POST":
            indID = request.POST['indID']
            individual = IndividualList.objects.get(id=indID)
            vacid = request.POST['vaccines']
            vaccineid = VaccineList.objects.get(id=vacid)

            vlocid = request.POST['vaccinelocations']
            vlocationid = VaccineLocationList.objects.get(id=vlocid)

            vactype = request.POST['VaccinationType']
            vacby = request.POST['VaccinatedBy']
            remark = request.POST['Remark']

            try:
                vachistlist = VaccineHistoryList.objects.create(members=memberid, individuals=individual, vaccines=vaccineid,
                                                            vaccinelocations=vlocationid, VaccinationType=vactype,
                                                            VaccinatedBy=vacby, Remark=remark)
                vachistlist.save()
                individual.Status = "Fully Vaccinated"
                individual.save()
                error="no"
            except:
                error="yes"

    return render(request, 'alreadyReg_Vaccine.html', locals())


def individual(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    indlist = IndividualList.objects.all()
    return render(request, 'individual.html', locals())


def viewIndividualDtls(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    individuals = IndividualList.objects.get(id=pid)
    vhistory = VaccineHistoryList.objects.filter(individuals=individuals)
    return render(request, 'viewIndividualDtls.html', locals())


def deleteIndividual(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    indilist = IndividualList.objects.get(id=pid)
    indilist.delete()
    return redirect('individual')


def vaccine(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vlist = VaccineList.objects.all()
    try:
        if request.method == "POST":
            name = request.POST['Name']
            status = request.POST['Status']

            try:
                VaccineList.objects.create(Name=name, Status=status)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'vaccine.html', locals())


def editVaccine(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    vlist = VaccineList.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['Name']
        status = request.POST['Status']

        vlist.Name = name
        vlist.Status = status

        try:
            vlist.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editVaccine.html', locals())


def deleteVaccine(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vlist = VaccineList.objects.get(id=pid)
    vlist.delete()
    return redirect('vaccine')


def vaccineArea(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vlocation = VaccineLocationList.objects.all()
    try:
        if request.method == "POST":
            location = request.POST['Location']
            status = request.POST['Status']

            try:
                VaccineLocationList.objects.create(Location=location, Status=status)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'vaccineArea.html', locals())


def editVaccineArea(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    vlocation = VaccineLocationList.objects.get(id=pid)
    if request.method == "POST":
        location = request.POST['Location']
        status = request.POST['Status']

        vlocation.Location = location
        vlocation.Status = status

        try:
            vlocation.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editVaccineArea.html', locals())


def deleteVaccineArea(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vlocation = VaccineLocationList.objects.get(id=pid)
    vlocation.delete()
    return redirect('vaccineArea')


def userList(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vlocation = VaccineLocationList.objects.all()
    memberlist = MemberList.objects.filter(Role = "Staff")
    try:
        error = ""
        if request.method == "POST":

            locid = request.POST['location']
            locationid = VaccineLocationList.objects.get(id=locid)

            fname = request.POST['FirstName']
            lname = request.POST['LastName']
            e = request.POST['EmailId']
            pwd = request.POST['Password']
            role = request.POST['Role']
            pic = request.FILES['Image']

            try:
                user = User.objects.create_user(username=e, password=pwd, first_name=fname, last_name=lname)
                MemberList.objects.create(user=user, location=locationid, Role=role, Image=pic)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'userList.html', locals())


def editUserList(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    vlocation = VaccineLocationList.objects.all()
    memberlist = MemberList.objects.get(id=pid)
    if request.method == "POST":
        locid = request.POST['location']
        locationid = VaccineLocationList.objects.get(id=locid)

        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        role = request.POST['Role']

        memberlist.user.first_name = fname
        memberlist.user.last_name = lname
        memberlist.location = locationid
        memberlist.Role = role

        try:
            memberlist.save()
            memberlist.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            pic = request.FILES['Image']
            memberlist.Image = pic
            memberlist.save()
        except:
            pass
    return render(request, 'editUserList.html', locals())


def deleteUserList(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    User.objects.get(id=pid).delete()
    return redirect('userList')


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def staff_login(request):
    error = ""
    if request.method == 'POST':
        email = request.POST['EmailId']
        pwd = request.POST['pwd']
        user = authenticate(username=email, password=pwd)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'staff_login.html', locals())


def sdashboard(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    totalvlist = VaccineList.objects.all().count()
    totalvcenter = VaccineLocationList.objects.all().count()
    totalfulvacc = IndividualList.objects.filter(Status='Fully Vaccinated').count()
    return render(request, 'sdashboard.html', locals())

def staffProfile(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    user = User.objects.get(id=request.user.id)
    memberlist = MemberList.objects.get(user=user)
    return render(request, 'staffProfile.html', locals())


def staffnew_Vaccine(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    vaccine = VaccineList.objects.filter(Status='Active')
    vlocation = VaccineLocationList.objects.filter(Status='Active')

    user = request.user
    memberid = MemberList.objects.get(user=user)

    if request.method == "POST":

        vacid = request.POST['vaccines']
        vaccineid = VaccineList.objects.get(id=vacid)

        vlocid = request.POST['vaccinelocations']
        vlocationid = VaccineLocationList.objects.get(id=vlocid)

        trackno = str(random.randint(100000000000000, 999999999999999))
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        gender = request.POST['Gender']
        dob = request.POST['DOB']
        contact = request.POST['Contact']
        address = request.POST['Address']
        vactype = request.POST['VaccinationType']
        vacby = request.POST['VaccinatedBy']
        remark = request.POST['Remark']
        status = request.POST['Status']

        try:
            individual = IndividualList.objects.create(FirstName=fname, LastName=lname, TrackingCode=trackno,
                                                       Gender=gender, DOB=dob, Contact=contact, Address=address,
                                                       Status=status)
            VaccineHistoryList.objects.create(members=memberid, individuals=individual, vaccines=vaccineid,
                                              vaccinelocations=vlocationid, VaccinationType=vactype, VaccinatedBy=vacby,
                                              Remark=remark)
            error = "no"
        except:
            error = "yes"
    return render(request, 'staffnew_Vaccine.html', locals())


def staffvaccineHistory(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')

    user = User.objects.get(id=request.user.id)
    member = MemberList.objects.get(user=user)

    #memberloc = member.location
    vachistory = VaccineHistoryList.objects.filter(members=member)

    return render(request, 'staffvaccineHistory.html', locals())


def staffviewHistory(request, pid):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    vhistory = VaccineHistoryList.objects.get(id=pid)
    return render(request, 'staffviewHistory.html', locals())


def staffalreadyReg_Vaccine(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    vaccine = VaccineList.objects.filter(Status='Active')
    vlocation = VaccineLocationList.objects.filter(Status='Active')
    indlist = None
    sd = None
    user = request.user
    memberid = MemberList.objects.get(user=user)

    try:
        if request.method == "POST":
            sd = request.POST['searchdata']
            indlist = IndividualList.objects.get(Q(TrackingCode=sd))
    except:
        if request.method == "POST":
            indID = request.POST['indID']
            individual = IndividualList.objects.get(id=indID)
            vacid = request.POST['vaccines']
            vaccineid = VaccineList.objects.get(id=vacid)

            vlocid = request.POST['vaccinelocations']
            vlocationid = VaccineLocationList.objects.get(id=vlocid)

            vactype = request.POST['VaccinationType']
            vacby = request.POST['VaccinatedBy']
            remark = request.POST['Remark']

            try:
                vachistlist = VaccineHistoryList.objects.create(members=memberid, individuals=individual,
                                                                vaccines=vaccineid,
                                                                vaccinelocations=vlocationid, VaccinationType=vactype,
                                                                VaccinatedBy=vacby, Remark=remark)
                vachistlist.save()
                individual.Status = "Fully Vaccinated"
                individual.save()
                error = "no"
            except:
                error = "yes"

    return render(request, 'staffalreadyReg_Vaccine.html', locals())


def staffindividual(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    indlist = IndividualList.objects.all()
    return render(request, 'staffindividual.html', locals())


def staffviewIndividualDtls(request, pid):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    individuals = IndividualList.objects.get(id=pid)
    vhistory = VaccineHistoryList.objects.filter(individuals=individuals)
    return render(request, 'staffviewIndividualDtls.html', locals())


def deletestaffIndividual(request, pid):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    indilist = IndividualList.objects.get(id=pid)
    indilist.delete()
    return redirect('staffindividual')

def staffchangePassword(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'staffchangePassword.html', locals())
