import uuid
from django.core.validators import RegexValidator
from django.db import models


class Patients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    medical_history = models.TextField()
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                   message="Enter a valid phone number starting with + and containing up to 15 digits.")],
    )
    email = models.EmailField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    objects = models.Manager()


# class AppointmentStatus(models.TextChoices):
#     SCHEDULED = 'scheduled', 'Scheduled'
#     COMPLETED = 'completed', 'Completed'
#     CANCELED = 'canceled', 'Canceled'

AppointmentStatus = (
    ('scheduled', 'Scheduled'),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled")
)


# class MedicalConditions(models.TextChoices):
#     DIABETES ='diabetes', 'Diabetes'
#     HYPERTENSION = 'hypertension', 'Hypertension'
#     ASTHMA = 'asthma', 'Asthma'
#     HEARTDISEASE = 'heartdisease', 'Heartdisease'
#     NONE = 'none', 'None'

MedicalConditions = (
    ('diabetes', 'Diabetes'),
    ('hypertension', 'Hypertension'),
    ('asthma', 'Asthma'),
    ('heart_disease', 'Heart_disease'),
    ('none', 'None')
)


class Appointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus,
        default='Scheduled'
    )
    medical_condition = models.CharField(
        max_length=20,
        choices=MedicalConditions,
        default='None'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with {self.doctor_name} for {self.patient.name} on {self.appointment_date}"

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    objects = models.Manager()
