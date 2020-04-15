from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from userapp.models import User, Consumer, Provider, ChargingStation, Vehicle, ChargingStationRecord, CsReport, ChargingStationWeekly,ChargePooler,MaintenanceManDetails,CsMaintenance
# Register your models here.
@admin.register(Vehicle)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(ChargingStation)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(ChargingStationRecord)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(ChargingStationWeekly)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(CsReport)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(ChargePooler)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Consumer)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Provider)
class ViewAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(Consumer)
# admin.site.register(Provider)
# admin.site.register(ChargingStation)
# admin.site.register(ChargingStationRecord)
# admin.site.register(ChargingStationWeekly)
admin.site.register(CsMaintenance)
admin.site.register(MaintenanceManDetails)

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('is_consumer','is_provider')}),
)

class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User,MyUserAdmin)