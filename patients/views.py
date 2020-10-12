from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView, FormView

from patients.forms import PatientForm


class PatientsPageView(TemplateView):
    template_name = 'patients/patients.html'


class PatientFormView(FormView):
    template_name = 'patients/patients_form.html'
    form_class = PatientForm
    success_url = '/'