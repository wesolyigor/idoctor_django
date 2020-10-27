from django.urls import path

from home.views import HomePageView
from patients.views import PatientsPageView, PatientFormView, PatientEmailFormView, PatientEditFormView

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients'),
    path('add/', PatientFormView.as_view(), name='patients_form'),
    path('add_email/', PatientEmailFormView.as_view(), name='patients_email_form'),
    path('edit/<int:id>/', PatientEditFormView.as_view(), name='patients_edit_form')

]
