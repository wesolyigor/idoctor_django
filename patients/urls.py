from django.urls import path

from home.views import HomePageView
from patients.views import PatientsPageView, PatientFormView

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients'),
    path('add/', PatientFormView.as_view(), name='patients_form')

]