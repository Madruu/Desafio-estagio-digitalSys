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
        personal_data_form = FormularioPersonalData(request.POST)
        contact_form = FormularioContato(request.POST)
        professional_experience_form = FormularioProfessionalExperience(request.POST)
        academic_formation_form = FormularioAcademicFormation(request.POST)

        if (personal_data_form.is_valid() and contact_form.is_valid() and 
                professional_experience_form.is_valid() and academic_formation_form.is_valid()):
            
            # Salvar dados pessoais
            personal_data = personal_data_form.save()
            # Salvar contato
            contact = contact_form.save()
            # Salvar experiência profissional
            professional_experience = professional_experience_form.save()
            # Salvar formação acadêmica
            academic_formation = academic_formation_form.save()

            # Criar o currículo associando todos os dados salvos
            curriculo = Curriculo.objects.create(
                curr_personal_data=personal_data,
                curr_contact=contact,
                curr_professional_experience=professional_experience,
                curr_academic_formation=academic_formation
            )

            #return redirect('get_all_curriculums')  # Redirecionar após sucesso
            return HttpResponse("Currículo criado com sucesso!")

    else:
        personal_data_form = FormularioPersonalData()
        contact_form = FormularioContato()
        professional_experience_form = FormularioProfessionalExperience()
        academic_formation_form = FormularioAcademicFormation()

    return render(request, 'recrutamento/send_application.html', {
        'personal_data_form': personal_data_form,
        'contact_form': contact_form,
        'professional_experience_form': professional_experience_form,
        'academic_formation_form': academic_formation_form,
    })
    
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
    return render(request, 'recrutamento/all_curriculums.html', context)

def confirm_delete_curriculum(request, curriculum_id):
    curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)

    return render(request, 'recrutamento/confirm_delete.html', {'curriculum_to_delete': curriculum_to_delete})    
   
def delete_curriculum(request, curriculum_id):

    if request.method == 'POST':
        curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)
        curriculum_to_delete.delete()
        return redirect('get_all_curriculums')
    
    
def update_curriculum(request, curriculum_id):
    curriculo = get_object_or_404(Curriculo, pk=curriculum_id)

    if request.method == 'POST':
        personal_data_form = FormularioPersonalData(request.POST, instance=curriculo.curr_personal_data)
        contact_form = FormularioContato(request.POST, instance=curriculo.curr_contact)
        professional_experience_form = FormularioProfessionalExperience(request.POST, instance=curriculo.curr_professional_experience)
        academic_formation_form = FormularioAcademicFormation(request.POST, instance=curriculo.curr_academic_formation)

        if (personal_data_form.is_valid() and contact_form.is_valid() and 
                professional_experience_form.is_valid() and academic_formation_form.is_valid()):
            
            personal_data_form.save()
            contact_form.save()
            professional_experience_form.save()
            academic_formation_form.save()
            
            # Redirecionar após a edição bem-sucedida
            return redirect('get_all_curriculums')  # Substitua 'success_page' pela URL desejada

    else:
        personal_data_form = FormularioPersonalData(instance=curriculo.curr_personal_data)
        contact_form = FormularioContato(instance=curriculo.curr_contact)
        professional_experience_form = FormularioProfessionalExperience(instance=curriculo.curr_professional_experience)
        academic_formation_form = FormularioAcademicFormation(instance=curriculo.curr_academic_formation)

    return render(request, 'recrutamento/edit_curriculum.html', {
        'personal_data_form': personal_data_form,
        'contact_form': contact_form,
        'professional_experience_form': professional_experience_form,
        'academic_formation_form': academic_formation_form,
        'curriculo': curriculo,  # Adicione para usar na exibição se necessário
    })
#def update_curriculum(request, curriculum_id):
#    curriculo = get_object_or_404(Curriculo, id=curriculum_id)

#    if request.method == 'POST':
#        form = CurriculumForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('get_all_curriculums')  # Redirecione para onde quiser após salvar
#    else:
#        form = CurriculumForm()

#    return render(request, 'edit_curriculum.html', {'form': form, 'curriculo': curriculo})