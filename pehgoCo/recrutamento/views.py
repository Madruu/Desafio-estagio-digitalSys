from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import PersonalData
from django.template import loader
from django.views import View
from .forms import FormularioPersonalData, FormularioContato, FormularioProfessionalExperience, FormularioAcademicFormation

# Create your views here.
def index(request):
    return HttpResponse("Este será o sistema de candidatos")

def candidates(request):
    all_candidates = PersonalData.objects.all()
    template = loader.get_template("recrutamento/candidatos.html")
    context = { 
        "all_candidates": all_candidates,
    }
    return HttpResponse(template.render(context, request))

def single_candidate(request, candidate_id):
    specific_candidate = get_object_or_404(PersonalData, pk=candidate_id)
    return render(request, "recrutamento/singlecandidato.html", {"specific_candidate": specific_candidate})

def get_curriculos(request):
    personal_data_form = FormularioPersonalData()
    contact_form = FormularioContato()
    professional_experience_form = FormularioProfessionalExperience()
    academic_formation_form = FormularioAcademicFormation()
    return render(request, 'recrutamento/all_curriculums.html', {
        'personal_data_form': personal_data_form,
        'contact_form': contact_form,
        'professional_experience_form': professional_experience_form,
        'academic_formation_form': academic_formation_form,
    })
    
def post_curriculos(request):
    personal_data_form = FormularioPersonalData(request.POST)
    contact_form = FormularioContato(request.POST)
    professional_experience_form = FormularioProfessionalExperience(request.POST)
    academic_formation_form = FormularioAcademicFormation(request.POST)
        
    if personal_data_form.is_valid() and contact_form.is_valid() and professional_experience_form.is_valid() and academic_formation_form.is_valid():
        personal_data_form.save()
        contact_form.save()
        professional_experience_form.save()
        academic_formation_form.save()
        return HttpResponse("Formulário enviado com sucesso!")
        
    return render(request, 'recrutamento/send_application.html', {
        'personal_data_form': personal_data_form,
        'contact_form': contact_form,
        'professional_experience_form': professional_experience_form,
        'academic_formation_form': academic_formation_form,
    })
