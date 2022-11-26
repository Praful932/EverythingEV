from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from userapp.models import (
    User,
    Consumer,
    Provider,
    ChargingStation,
    Vehicle,
    ChargingStationRecord,
    CsReport,
    ChargingStationWeekly,
    ChargePooler,
    MaintenanceManDetails,
    CsMaintenance,
    Support,
    UserRecord,
    Survey,
    User_convert_specs,
    CovertSpecs,
    DrivingEnv,
)

# Register your models here.
@admin.register(Vehicle)
class Vehicle(ImportExportModelAdmin):
    pass


@admin.register(DrivingEnv)
class DrivingEnv(ImportExportModelAdmin):
    pass


@admin.register(ChargingStation)
class ChargingStation(ImportExportModelAdmin):
    pass


@admin.register(CovertSpecs)
class CovertSpecs(ImportExportModelAdmin):
    pass


@admin.register(User_convert_specs)
class User_convert_specs(ImportExportModelAdmin):
    pass


@admin.register(ChargingStationRecord)
class ChargingStationRecord(ImportExportModelAdmin):
    pass


@admin.register(ChargingStationWeekly)
class ChargingStationWeekly(ImportExportModelAdmin):
    pass


@admin.register(CsReport)
class CsReport(ImportExportModelAdmin):
    pass


@admin.register(ChargePooler)
class ChargePooler(ImportExportModelAdmin):
    pass


@admin.register(Consumer)
class Consumer(ImportExportModelAdmin):
    pass


@admin.register(Provider)
class Provider(ImportExportModelAdmin):
    pass


@admin.register(CsMaintenance)
class CsMaintenance(ImportExportModelAdmin):
    pass


@admin.register(MaintenanceManDetails)
class MaintenanceManDetails(ImportExportModelAdmin):
    pass


# admin.site.register(Consumer)
# admin.site.register(Provider)
# admin.site.register(ChargingStation)
# admin.site.register(ChargingStationRecord)
# admin.site.register(ChargingStationWeekly)
# admin.site.register(CsMaintenance)
# admin.site.register(MaintenanceManDetails)
admin.site.register(Support)
admin.site.register(UserRecord)
admin.site.register(Survey)
ADDITIONAL_USER_FIELDS = ((None, {"fields": ("is_consumer", "is_provider")}),)


@admin.register(User)
class MyUserAdmin(UserAdmin, ImportExportModelAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


# admin.site.register(User, MyUserAdmin)
