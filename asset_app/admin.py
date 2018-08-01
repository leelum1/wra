from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User, Computer, Employee, Equipment, Vehicle

class NewUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class NewUserAdmin(UserAdmin):
    form = NewUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_no', 'is_watershed', 'is_abstractor', 'is_operations', 'is_licensing', 'is_management',)}),
    )

class ComputerAdmin(admin.ModelAdmin):
    list_display = ['comp_no', 'emp_no', 'comp_type']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'first_name', 'last_name', 'designation']

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'storage']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vim', 'licence_plate', 'model']

# Register your models here.
admin.site.register(User, NewUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Vehicle, VehicleAdmin)
