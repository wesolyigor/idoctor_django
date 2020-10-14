from django.urls import path

from home.views import HomePageView
from patients.views import PatientsPageView, PatientFormView, patient_form_view

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients'),
    path('add/', patient_form_view, name='patients_form')

]