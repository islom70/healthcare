from django.urls import path

from blog.views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView, \
    AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView

urlpatterns = [
    path('patients/list/', PatientListView.as_view(), name='patient-list'),
    path('patient/detail/<uuid:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/update/<int:pk>/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient-delete'),


    path('appointments/list/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointment/detail/<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointments/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment-delete')
]