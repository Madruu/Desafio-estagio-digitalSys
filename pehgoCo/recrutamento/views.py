from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation, Curriculo
from django.template import loader
from django.views import View
from .forms import FormularioPersonalData, FormularioContato, FormularioProfessionalExperience, FormularioAcademicFormation, CurriculumForm
from django.contrib import messages

# Página inicial
def index(request):
    return HttpResponse("Este será o sistema de candidatos")

#====================================================================================================================================================================
#CANDIDATOS
#Retorna todos os candidatos
def candidates(request):
    all_candidates = PersonalData.objects.all()
    template = loader.get_template("recrutamento/candidatos.html")
    context = { 
        "all_candidates": all_candidates,
    }
    return HttpResponse(template.render(context, request))

#Retorna um candidato baseado em seu Id
def single_candidate(request, candidate_id):
    specific_candidate = get_object_or_404(PersonalData, pk=candidate_id)
    return render(request, "recrutamento/singlecandidato.html", {"specific_candidate": specific_candidate})

#Deleta candidato baseado em seu Id
def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(PersonalData, pk=candidate_id)
    candidate.delete()
    return HttpResponse("Candidato deletado com sucesso!")

#====================================================================================================================================================================
#CURRICULOS
#Cria curriculos

def post_curriculos(request):
    if request.method == 'POST':
        curriculum_data = CurriculumForm(request.POST)
        if curriculum_data.is_valid():
            curriculum_data.save()
            return HttpResponse("Formulario cadastrado com sucesso!")
    else:
        curriculum_data = CurriculumForm()

    return render(request, 'recrutamento/send_application.html', {'curriculum_data': curriculum_data})

def get_single_curriculum(request, curriculum_id):
    try:
        specific_curriculum = Curriculo.objects.get(pk=curriculum_id)
    except Curriculo.DoesNotExist:
        specific_curriculum = None  # Define como None se não existir
    
    context = {
        'specific_curriculum': specific_curriculum,
    }
    return render(request, 'recrutamento/single_curriculum.html', context)

#Pega todos os curriculos
def get_all_curriculums(request):
    curriculos = Curriculo.objects.all()
    context = {
        'curriculos': curriculos,
    }
    template = loader.get_template('recrutamento/all_curriculums.html')
    return HttpResponse(template.render(context, request))

def confirm_delete_curriculum(request, curriculum_id):
    #curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)

#    if request.method == 'POST':
#       curriculum_to_delete.delete()
#       return redirect('delete_curriculum')  # Redirecione para uma página de sucesso ou lista de currículos
    curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)

    return render(request, 'recrutamento/confirm_delete.html', {'curriculum_to_delete': curriculum_to_delete})    
    #return render(request, 'recrutamento/confirm_delete.html', {'curriculum': curriculum_to_delete})

def delete_curriculum(request, curriculum_id):

    if request.method == 'POST':
        curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)
        curriculum_to_delete.delete()
        return redirect('get_all_curriculums')
    
#def update_curriculum(request, curriculum_id):
#    curriculum = get_object_or_404(Curriculo, pk=curriculum_id)
#    form = CurriculumForm(request.POST or None, instance=curriculum)
#    if form.is_valid():
#        form.save()
#        return redirect('get_all_curriculums')
#    return render(request, 'recrutamento/send_application.html', {'form': form})

