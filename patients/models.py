from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    personal_identity_number = models.IntegerField(unique=True)
    sex = models.CharField(choices=[('0', 'male'), ('1', 'female'), ('2', 'other')], max_length=255)

    # patient_email_id = models.ForeignKey(PatientEmail, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} identity number: {self.personal_identity_number}'


class PatientEmail(models.Model):
    email = models.EmailField(max_length=100)
    patient_id = models.ForeignKey(Patient,
                                   on_delete=models.CASCADE)  # kaskada - jak usuniemy id to usuwamy wszystkie śmieci

    def __str__(self):
        return f"{self.patient_id.first_name} {self.patient_id.last_name}. Email Email {self.email}"


