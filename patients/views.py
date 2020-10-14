from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView, FormView

from patients.forms import PatientForm, PatientEmailForm


class PatientsPageView(TemplateView):
    template_name = 'patients/patients.html'


class PatientFormView(FormView):
    template_name = 'patients/patients_form.html'
    form_class = PatientForm, PatientEmailForm
    success_url = '/'


def patient_form_view(request):
    if request.method == 'POST':
        pef = PatientEmailForm(request.POST)
        pf = PatientForm(request.POST)

        if pf.is_valid() and pef.is_valid():
            x = pf.save()
            pef = PatientEmailForm({**{'patient_id': x.id}, **request.POST})
            z = pef.save()
            print(z.patient_id)

    else:
        pf = PatientForm()
        pef = PatientEmailForm()

    return render(request, 'patients/patients_form.html', {'pef': pef, 'pf': pf})
