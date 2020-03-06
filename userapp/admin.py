from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from userapp.models import User, Consumer, Provider, ChargingStation, Vehicle,ChargingStationRecord,CsReport
# Register your models here.
@admin.register(Vehicle)
class ViewAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Consumer)
admin.site.register(Provider)
admin.site.register(ChargingStation)
admin.site.register(ChargingStationRecord)
admin.site.register(CsReport)

# admin.site.register(Vehicle)
ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('is_consumer','is_provider')}),
)

class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User,MyUserAdmin)