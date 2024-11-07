from rest_framework import serializers
from .models import Patients, Appointments


class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['id', 'name', 'age', 'medical_history']


class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['name', 'age', 'medical_history', 'phone', 'email', 'address']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['contact_info'] = {
            'phone': representation.pop('phone'),
            'email': representation.pop('email'),
            'address': representation.pop('address')
        }
        return representation


class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['name', 'age', 'medical_history', 'contact_info']


class AppointmentListSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = Appointments
        fields = ['patient', 'doctor_name', 'appointment_date']

    def get_patient(self, obj):
        return obj.patient.name


class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['patient', 'doctor_name', 'appointment_date', 'status', 'medical_condition']


class AppointmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['patient', 'doctor_name', 'appointment_date', 'status', 'medical_condition']
