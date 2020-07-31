from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from geopy.geocoders import Nominatim
from django.urls import reverse_lazy
from django.db.models import Case, When
from userapp.forms import (UserSignUpForm, ConsumerSignUpForm, ProviderSignUpForm, UserUpdateForm,
                           ChargingStationForm, SupportForm, CharpoolerForm)
from django.contrib.auth import logout, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from userapp.models import (User, Provider, ChargingStation, ChargingStationRecord, CsReport, ChargingStationWeekly,
                            ChargePooler, MaintenanceManDetails, Consumer, CsMaintenance, Vehicle)
from django.http import JsonResponse
from django.core.mail import send_mail
from Sih.settings import EMAIL_HOST_USER
from userapp.helper import get_user_location
import json
import math


def get_distance(lat_1, lng_1, lat_2, lng_2):
    d_lat = lat_2 - lat_1
    d_lng = lng_2 - lng_1

    temp = (
        math.sin(d_lat / 2) ** 2
        + math.cos(lat_1)
        * math.cos(lat_2)
        * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))


def check(request):
    if request.user.is_provider:
        return redirect('dash-welcome')
    return redirect('index')


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            if username == "admin":
                pass
            elif Consumer.objects.get(user=request.user):
                pass
        except Consumer.DoesNotExist:
            try:
                if Provider.objects.get(user=request.user):
                    pass
            except Provider.DoesNotExist:
                return redirect('registerConsumerSocial')
    return render(request, "userapp/index.html")


@login_required
def registerConsumerSocial(request):
    if request.method == 'POST':
        consumerform = ConsumerSignUpForm(request.POST)
        if consumerform.is_valid():
            new_user = User.objects.get(username=request.user.username)
            new_user.is_consumer = True
            consumer = consumerform.save(commit=False)
            consumer.user = new_user
            new_user.save()
            consumerform.save()
            return redirect('index')
    else:
        if not request.user.is_consumer and not request.user.is_provider:
            redirect('index')
        consumerform = ConsumerSignUpForm()
    context = {
        'consumerform': consumerform
    }
    return render(request, "userapp/registerConsumer.html", context=context)


def register(request):
    return render(request, "userapp/registration_page.html")


def registerConsumer(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        signupform = UserSignUpForm(request.POST)
        consumerform = ConsumerSignUpForm(request.POST)
        if signupform.is_valid() and consumerform.is_valid():
            new_user = signupform.save(commit=False)
            new_user.is_consumer = True
            new_user = signupform.save()
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            consumer = consumerform.save(commit=False)
            consumer.user = new_user
            consumerform.save()
            return redirect('index')
    else:
        signupform = UserSignUpForm()
        consumerform = ConsumerSignUpForm()
    context = {
        'signupform': signupform,
        'consumerform': consumerform
    }
    return render(request, "userapp/registerConsumer.html", context=context)


def registerProvider(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        signupform = UserSignUpForm(request.POST)
        providerform = ProviderSignUpForm(request.POST, request.FILES)
        if signupform.is_valid() and providerform.is_valid():
            new_user = signupform.save(commit=False)
            new_user.is_provider = True
            new_user = signupform.save()
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            consumer = providerform.save(commit=False)
            consumer.user = new_user
            providerform.save()
            return redirect('index')
    else:
        signupform = UserSignUpForm()
        providerform = ProviderSignUpForm()
    context = {
        'signupform': signupform,
        'providerform': providerform
    }
    return render(request, "userapp/registerProvider.html", context=context)


def logoutf(request):
    # Check if user is logged in if not redirect to login page
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    return redirect('login')


@login_required
def UpdateProfile(request):
    supportform = 0
    if request.method == "GET":
        if request.user.is_consumer:
            userform = UserUpdateForm(instance=request.user)
            fieldform = ConsumerSignUpForm(instance=request.user.consumer)
        else:
            userform = UserUpdateForm(instance=request.user)
            fieldform = ProviderSignUpForm(instance=request.user.provider)
            supportform = SupportForm()
        context = {
            'userform': userform,
            'fieldform': fieldform,
            'supportform': supportform
        }
    else:
        if request.user.is_consumer:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = ConsumerSignUpForm(
                request.POST, instance=request.user.consumer)
        else:
            userform = UserUpdateForm(request.POST, instance=request.user)
            fieldform = ProviderSignUpForm(
                request.POST, request.FILES, instance=request.user.provider)
        if userform.is_valid() and fieldform.is_valid():
            userform.save()
            fieldform.save()
            return redirect('index')
    if request.user.is_consumer:
        return render(request, "userapp/updateprofile.html", context=context)
    return render(request, "userapp/provider_profile.html", context=context)


@login_required
def AddChargingStation(request):
    if request.user.is_consumer:
        return redirect('index')
    else:
        if request.method == 'POST':
            stationform = ChargingStationForm(request.POST, request.FILES)
            if stationform.is_valid():
                ob = stationform.save(commit=False)
                provider = Provider.objects.get(user=request.user)
                ob.owner = provider
                lat = stationform.cleaned_data['lat']
                lng = stationform.cleaned_data['lng']
                geolocator = Nominatim(user_agent='EV')
                location = geolocator.reverse(str(lat)+', ' + str(lng))
                try:
                    ob.city = location.raw['address']['city']
                except LookupError:
                    ob.city = location.raw['address']['state_district']
                try:
                    ob.suburb = location.raw['address']['suburb']
                except LookupError:
                    try:
                        ob.suburb = location.raw['address']['county']
                    except LookupError:
                        ob.suburb = location.raw['address']['town']
                stationform.save()
                return redirect('Provider-Dashboard')
        else:
            stationform = ChargingStationForm()
            stationform.fields['lat'].widget = forms.HiddenInput()
            stationform.fields['lng'].widget = forms.HiddenInput()
    context = {
        'stationform': stationform
    }
    return render(request, "userapp/add_charging_station.html", context=context)


@login_required
def ProviderDashboard(request):
    supportform = 0
    if request.user.provider:
        if request.method == 'GET':
            current_provider = Provider.objects.get(user=request.user)
            page = request.GET.get('page', 1)
            paginator = Paginator(ChargingStation.objects.filter(owner=current_provider), 3)
            try:
                cslist = paginator.page(page)
            except PageNotAnInteger:
                cslist = paginator.page(1)
            except EmptyPage:
                cslist = paginator.page(paginator.num_pages)
            supportform = SupportForm()
            context = {
                'cslist': cslist,
                'supportform': supportform
            }
            return render(request, "userapp/provider_dashboard.html", context=context)
    return redirect('index')


class ChargingStationProviderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ChargingStation
    success_url = reverse_lazy('Provider-Dashboard')

    # Check if current user is author
    def test_func(self):
        cs = self.get_object()
        if self.request.user.is_provider and (cs.owner.user == self.request.user):
            return True
        return False


@login_required
def ChargingStationConsumer(request):
    lat_user, lng_user = get_user_location()
    cslist = ChargingStation.objects.all()
    distid_list = []
    pkid = []
    for ids in cslist:
        pkid.append(ids.pk)

    for cs in cslist:
        # Convert degree to radians
        lat_cs, lng_cs = map(math.radians, [float(cs.lat), float(cs.lng)])
        distance = get_distance(lat_user, lng_user, lat_cs, lng_cs)
        distid_list.append([distance, cs.pk])
    distid_list.sort()
    # Sorted id of Charging Station according to user location
    id_list = [x[1] for x in distid_list]
    name_cleaned = []
    city_cleaned = []
    suburb_cleaned = []
    owner_cleaned = []
    lngs_cleaned = []
    lats_cleaned = []
    ports_cleaned = []
    dc_cleaned = []
    ac_cleaned = []
    price_cleaned = []
    restroom_cleaned = []
    cctv_cleaned = []
    closing_cleaned = []
    opening_cleaned = []
    for cs in cslist:
        name_cleaned.append(str(cs.name))
        city_cleaned.append(str(cs.city))
        suburb_cleaned.append(str(cs.suburb))
        owner_cleaned.append(str(cs.owner.user.username))
        lats_cleaned.append(float(cs.lat))
        lngs_cleaned.append(float(cs.lng))
        ports_cleaned.append(int(cs.no_of_ports))
        dc_cleaned.append(int(cs.fast_dc))
        ac_cleaned.append(int(cs.slow_ac))
        price_cleaned.append(float(cs.price_kwh))
        restroom_cleaned.append(int(cs.restroom))
        cctv_cleaned.append(int(cs.cctv))
        opening_cleaned.append(str(cs.opening_time))
        closing_cleaned.append(str(cs.closing_time))
    csdata = [list(x) for x in zip(
        name_cleaned, city_cleaned, suburb_cleaned, owner_cleaned,
        lats_cleaned, lngs_cleaned, ports_cleaned, dc_cleaned,
        ac_cleaned, price_cleaned, restroom_cleaned, cctv_cleaned,
        opening_cleaned, closing_cleaned)]
    # Get all objects according to id
    # to preserve order SO!
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(id_list)])
    cslist = ChargingStation.objects.filter(pk__in=id_list).order_by(preserved)
    context = {
        'csdata': json.dumps(csdata),
        'cslist': cslist,
        'pkid': json.dumps(pkid)
    }
    return render(request, 'userapp/consumer_charging_stations.html', context=context)
    return redirect('index')


@login_required
def ChargingStationAnalytics(request, pk):
    if request.user.is_provider:
        current_cs = ChargingStation.objects.get(id=pk)
        # how many consumers visited this charging station
        reportcount = ChargingStationRecord.objects.filter(cs=current_cs).count()
        # find one sample csreport of current charging station
        report = CsReport.objects.filter(cs=current_cs)[0]
        freq = []
        for i in range(24):
            # getattr to access changing field anme
            freq.append(getattr(report, 't'+str(i)))
        wholecs = ChargingStationRecord.objects.filter(cs=current_cs)
        consumption = []
        total_consumption = 0
        total_revenue = 0
        for ele in wholecs:
            total_consumption += float(ele.vehicle.charging_rate) * (ele.duration/60)
        total_consumption = round(total_consumption, 2)
        total_revenue = round(total_consumption * float(current_cs.price_kwh), 2)
        csrecord = ChargingStationRecord.objects.filter(cs=current_cs)
        s = 0
        n = 0
        for cs in csrecord:
            n += 1
            s = s + cs.elec_consumption
        consumption.append(s)
        weekreport = ChargingStationWeekly.objects.filter(cs=current_cs)[0]
        wr = []
        for i in range(7):
            wr.append(getattr(weekreport, 'd'+str(i+1)))
        supportform = SupportForm()
        context = {
            'totalcount': reportcount,
            'freq': json.dumps(freq),
            'consumption': json.dumps(consumption),
            'wr': json.dumps(wr),
            'supportform': supportform,
            'total_revenue': round(total_revenue, 2),
            'total_consumption': total_consumption
        }
        return render(request, "userapp/cs_analytics.html", context=context)
    return redirect('index')


@login_required
def ChargingStationDashboard(request, pk):
    if request.user.is_provider:
        current_cs = ChargingStation.objects.get(id=pk)
        # get all records of the current_cs
        allrecords = ChargingStationRecord.objects.filter(cs=current_cs)
        username_cleaned = []
        vehicle_cleaned = []
        duration_cleaned = []
        consumption_cleaned = []
        for record in allrecords:
            username_cleaned.append(str(record.consumer.user.username))
            vehicle_cleaned.append(str(record.vehicle.company))
            duration_cleaned.append(int(record.duration))
            consumption_cleaned.append(int(record.elec_consumption))
        recorddata = [list(x) for x in zip(username_cleaned,
                                           vehicle_cleaned, duration_cleaned, consumption_cleaned)]
        supportform = SupportForm()
        context = {
            'records': recorddata,
            'supportform': supportform,
        }
        return render(request, "userapp/dash_welcome.html", context=context)
    return redirect('index')


@login_required
def ChargePooling(request):
    if request.user.is_consumer:
        chargepoolers = ChargePooler.objects.all()
        context = {
            'chargepoolers': chargepoolers
        }
        return render(request, "userapp/chargepoolerpage.html", context=context)
    poolerform = CharpoolerForm()

    return render(request, "chargepoolingform.html", {'form': poolerform})


@login_required
def RouteYourWay(request):
    if request.user.is_consumer:
        cslist = ChargingStation.objects.all()
        # Sorted id of Charging Station according to user location
        name_cleaned = []
        city_cleaned = []
        suburb_cleaned = []
        owner_cleaned = []
        lngs_cleaned = []
        lats_cleaned = []
        ports_cleaned = []
        dc_cleaned = []
        ac_cleaned = []
        price_cleaned = []
        restroom_cleaned = []
        cctv_cleaned = []
        closing_cleaned = []
        opening_cleaned = []
        for cs in cslist:
            name_cleaned.append(str(cs.name))
            city_cleaned.append(str(cs.city))
            suburb_cleaned.append(str(cs.suburb))
            owner_cleaned.append(str(cs.owner.user.username))
            lats_cleaned.append(float(cs.lat))
            lngs_cleaned.append(float(cs.lng))
            ports_cleaned.append(int(cs.no_of_ports))
            dc_cleaned.append(int(cs.fast_dc))
            ac_cleaned.append(int(cs.slow_ac))
            price_cleaned.append(float(cs.price_kwh))
            restroom_cleaned.append(int(cs.restroom))
            cctv_cleaned.append(int(cs.cctv))
            opening_cleaned.append(str(cs.opening_time))
            closing_cleaned.append(str(cs.closing_time))
        csdata = [list(x) for x in zip(
            name_cleaned, city_cleaned, suburb_cleaned, owner_cleaned,
            lats_cleaned, lngs_cleaned, ports_cleaned, dc_cleaned,
            ac_cleaned, price_cleaned, restroom_cleaned, cctv_cleaned,
            opening_cleaned, closing_cleaned)]
        context = {
            'csdata': json.dumps(csdata),
        }
        return render(request, "userapp/routeyourway.html", context=context)
    return redirect('index')


class MaintenanceMan(CreateView):
    model = MaintenanceManDetails
    template_name = 'MaintenanceManForm.html'
    fields = ['name', 'OrgName', 'ph1', 'ph2', 'OfficeAdd', 'City', 'AreaLocality']

    def form_valid(self, form):
        form.instance.own = self.request.user.provider
        return super().form_valid(form)


@login_required
def bookMaintenanceMan(request, pk):
    cscount = ChargingStation.objects.filter(owner=request.user.provider)
    if request.user.is_provider:
        if request.method == 'POST':
            if request.POST.get('problem'):
                CsM = CsMaintenance()
                # get the id from url for maintenance
                # get reused
                # get description
                CsM.csm = request.user.provider
                CsM.Mm_id = pk
                CsM.Problem = request.POST.get('problem')
                CsM.ph = request.POST.get('phone')
                cname = request.POST.get('Cs')
                c = ChargingStation.objects.filter(name=cname)[0]
                CsM.CsSelect = c
                CsM.save()
                return redirect('dash-welcome')
        return render(request, "booking.html", {'cs': cscount})


class SearchListView(ListView):
    model = MaintenanceManDetails
    template_name = 'userapp/MaintainManTable.html'
    context_object_name = 'd'


def MaintenanceDashboard(request):
    if request.user.is_provider:
        supportform = SupportForm()
        context = {
            'supportform': supportform
        }
        return render(request, "userapp/maintenance_dashboard.html", context=context)


class ComplaintsListView(ListView):
    model = CsMaintenance
    template_name = 'userapp/complaint_dashboard.html'
    context_object_name = 'd'


@login_required
def MaintenanceComplaint(request):
    m = MaintenanceManDetails.objects.get(own=request.user.provider)
    if request.method == 'POST':
        visited = request.POST.get('visited')
        CsMaintenance.objects.get(pk=visited).delete()
        m.CompletedComplaints += 1
        return redirect('dash-welcome')
    d = m.jobs.all()
    locate = CsMaintenance.objects.filter(Mm=m.id)
    count = m.jobs.count()
    lngs_cleaned = []
    lats_cleaned = []
    pk_cleaned = []
    name_cleaned = []
    for l in locate:
        lats_cleaned.append(float(l.CsSelect.lat))
        lngs_cleaned.append(float(l.CsSelect.lng))
        pk_cleaned.append(int(l.CsSelect.pk))
        name_cleaned.append(str(l.CsSelect.name))
    js_data = [list(x) for x in zip(
        lats_cleaned, lngs_cleaned, pk_cleaned, name_cleaned
    )]

    total = count+m.CompletedComplaints
    supportform = SupportForm()
    return render(request, "userapp/complaint_dashboard.html", {'d': d, 'count': count, 'm': m,
                                                                'total': total, "my_data": json.dumps(js_data),
                                                                'supportform': supportform})


def PendingComplaintsListView(request):
    supportform = SupportForm()
    context = {
        'supportform': supportform
    }
    return render(request, "userapp/complaint_dashboard.html", context=context)


def PendingComplaints(request):
    supportform = SupportForm()
    context = {
        'supportform': supportform
    }
    return render(request, "userapp/complaint_dashboard.html", context=context)


def SupportRequest(request):
    if request.method == "POST" and request.is_ajax():
        subject = request.POST.get('subject', None)
        description = request.POST.get('description', None)
        support = {
            'subject': subject,
            'description': description
        }
        support = json.dumps(support)
        send_mail(
            'Support Request', support,
            EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False
        )
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)


def faq(request):
    supportform = SupportForm()
    context = {
        'supportform': supportform
    }
    return render(request, "userapp/FAQs.html", context=context)


def WhyChooseEV(request):
    supportform = SupportForm()
    context = {
        'supportform': supportform
    }
    return render(request, "userapp/why_choose_ev.html", context=context)


def salesPage(request):
    return render(request, "userapp/sales_home.html")


def twoWheelers(request):
    return render(request, "userapp/2w.html")


def threeWheelers(request):
    return render(request, "userapp/3w.html")


def fourWheelers(request):
    return render(request, "userapp/4w.html")


def heavyVehicles(request):
    return render(request, "userapp/heavy-vehicles.html")


def BuildCs(request):
    return render(request, "buildchargingstation.html")


def savingsCalculator(request):
    company = Vehicle.objects.all()
    return render(request, "userapp/savings_calculator.html", {"Vehicle": company})


@login_required
def dashwelcome(request):
    if request.user.is_provider:
        current_provider = request.user.provider
        all_cs = current_provider.ownerof.all()
        try:
            if request.user.provider.maintenancemandetails:
                pass
        except MaintenanceManDetails.DoesNotExist:
            pass
        # If only Maintainance not CS Owner
        if not all_cs:
            return redirect('Complaint-Dashboard')
        total_visits = 0
        total_consumption = 0
        total_revenue = 0
        best_revenue = 0
        best_cs = ""
        for cs in all_cs:
            all_record_cs = cs.csrecord.all()
            consumption_cs = 0
            for record in all_record_cs:
                total_visits += 1
                consumption_cs += float(record.vehicle.charging_rate) * (record.duration/60)
            currentcs_revenue = float(cs.price_kwh) * consumption_cs
            if currentcs_revenue > best_revenue:
                best_cs = cs.name
                best_revenue = currentcs_revenue
            total_revenue += currentcs_revenue
            total_consumption += consumption_cs
        supportform = SupportForm()
        context = {
            'supportform': supportform,
            'total_visits': total_visits,
            'total_revenue': round(total_revenue, 2),
            'total_consumption': round(total_consumption, 2),
            'best_revenue': round(best_revenue, 2),
            'best_cs': best_cs
        }
        return render(request, "userapp/dash_welcome.html", context=context)
    else:
        # To Meme
        return redirect('index')


@login_required
def live_data(request):
    if not request.user.is_consumer and not request.user.is_provider:
        return render(request, "userapp/live_data.html")
    return redirect('index')

@login_required
def demo(request):
    c = ChargingStation.objects.all()
    for cs in c:
        v= CsReport()
        v.cs = cs
        v.time = "2000-12-11"
        v.t0 = random.randrange(00, 15, 2)
        v.t1 = random.randrange(00, 15, 2)
        v.t2 = random.randrange(00, 15, 2)
        v.t3 = random.randrange(00, 15, 2)
        v.t4 = random.randrange(00, 15, 2)
        v.t5 = random.randrange(00, 15, 2)
        v.t6 = random.randrange(00, 15, 2)
        v.t7 = random.randrange(00, 15, 2)
        v.t8 = random.randrange(00, 15, 2)
        v.t9 = random.randrange(00, 15, 2)
        v.t10 = random.randrange(00, 15, 2)
        v.t11 = random.randrange(00, 15, 2)
        v.t12 = random.randrange(00, 15, 2)
        v.t13 = random.randrange(00, 15, 2)
        v.t14 = random.randrange(00, 15, 2)
        v.t15 = random.randrange(00, 15, 2)
        v.t16 = random.randrange(00, 15, 2)
        v.t17 = random.randrange(00, 15, 2)
        v.t18 = random.randrange(00, 15, 2)
        v.t19 = random.randrange(00, 15, 2)
        v.t20 = random.randrange(00, 15, 2)
        v.t21 = random.randrange(00, 15, 2)
        v.t22 = random.randrange(00, 15, 2)
        v.t23 = random.randrange(00, 15, 2)
        v.save()

    return HttpResponse("hii") 
