from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patients, Appointments
from .serializers import PatientListSerializer, PatientDetailSerializer, PatientCreateSerializer, \
    PatientUpdateSerializer, AppointmentListSerializer, AppointmentDetailSerializer, AppointmentCreateSerializer, \
    AppointmentUpdateSerializer


class PatientListView(APIView):
    def get(self, request):
        patients = Patients.objects.all()
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PatientDetailView(APIView):
    def get(self, request, pk):
        try:
            patient = Patients.objects.get(pk=pk)
            serializer = PatientDetailSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patients.DoesNotExist:
            return Response({"detail": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)


class PatientCreateView(APIView):
    def post(self, request):
        serializer = PatientCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientUpdateView(APIView):
    def update(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        serializer = PatientUpdateSerializer(instance=patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PatientDeleteView(APIView):
    def delete(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        patient.delete()
        return Response('Data deleted successfully', status=status.HTTP_204_NO_CONTENT)


class AppointmentListView(APIView):
    def get(self, request):
        appointments = Appointments.objects.all()
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentDetailView(APIView):
    def get(self, request, pk):
        try:
            appointment = Appointments.objects.get(pk=pk)
            serializer = AppointmentDetailSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Appointments.DoesNotExist:
            return Response({"detail": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)


class AppointmentCreateView(APIView):
    def post(self, request):
        serializer = AppointmentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentUpdateView(APIView):
    def post(self, request, pk):
        appointment = Appointments.objects.get(pk=pk)
        serializer = AppointmentUpdateSerializer(instance=appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class AppointmentDeleteView(APIView):
    def delete(self, request, pk):
        appointment = Appointments.objects.get(pk=pk)
        appointment.delete()




