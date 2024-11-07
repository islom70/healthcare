from django.contrib import admin
from .models import Patients, Appointments


class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'medical_history', 'phone', 'email', 'address', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'age', 'phone', 'email', 'address', 'created_at', 'updated_at')


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor_name', 'appointment_date', 'created_at', 'updated_at')
    search_fields = ('id', 'patient', 'doctor_name', 'appointment_date', 'created_at', 'updated_at')


admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(Patients, PatientsAdmin)

