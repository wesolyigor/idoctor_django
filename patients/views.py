from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.views import View

from django.views.generic import TemplateView, FormView

from patients.forms import PatientForm, PatientEmailForm
from patients.models import Patient, PatientEmail


class PatientsPageView(View):
    def get(self, request):
        data = Patient.objects.annotate(email=F('patientemail__email')).values('pk', 'first_name', 'last_name', 'email',
                                                                               'date_of_birth',
                                                                               'personal_identity_number')
        # data = PatientEmail.objects.all().prefetch_related('patient_id')
        # print(vars(data))
        # for p in data:
        #     print(p)
        print(20 * 'x')
        return render(request, "patients/patients.html", context={"data": data})


class PatientFormView(FormView):
    template_name = 'patients/patients_form.html'
    form_class = PatientForm
    success_url = '/patients/add_email'

    def form_valid(self, form):
        """
        implementacja sesji w django
        """
        patient = form.save()
        self.request.session['patient'] = patient.pk
        return super().form_valid(form)


class PatientEmailFormView(FormView):
    template_name = 'patients/patients_email_form.html'
    form_class = PatientEmailForm
    success_url = '/patients'

    def form_valid(self, form):
        patient = self.request.session.get('patient')
        obj = Patient.objects.get(id=patient)
        # x = patient.save(commit=False)
        y = form.save(commit=False)
        y.patient_id = obj
        # x.save()
        y.save()

        return super().form_valid(form)


class PatientEditFormView(View):
    def get(self, request, id):
        print(id)
        print(type(id))
        data = Patient.objects.get(pk=id)
        form = PatientForm(instance=data) # parametr konieczny do wyświetlenia, podajemy tam parametr z obiektem

        return render(request, "patients/patients_form.html", {'form': form})

# def patient_form_view(request):
#     if request.method == 'POST':
#         pef = PatientEmailForm(request.POST)
#         pf = PatientForm(request.POST)
#
#         if pf.is_valid() and pef.is_valid():
#             x = pf.save()
#             pef = PatientEmailForm({**{'patient_id': x.id}, **request.POST})
#             z = pef.save()
#             print(z.patient_id)
#
#     # TODO - progressive enhancement
#
#     else:
#         pf = PatientForm()
#         pef = PatientEmailForm()
#
#     return render(request, 'patients/patients_form.html', {'pef': pef, 'pf': pf})
