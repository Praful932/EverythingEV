from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import User, Consumer, Provider, ChargingStation, Vehicle, ChargingStationRecord
# Register your models here.

admin.site.register(Consumer)
admin.site.register(Provider)
admin.site.register(ChargingStation)
admin.site.register(Vehicle)
admin.site.register(ChargingStationRecord)
ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('is_consumer','is_provider')}),
)

class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User,MyUserAdmin)