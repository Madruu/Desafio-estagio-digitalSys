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
def favicon_view(request):
    return HttpResponse(status=204)

#====================================================================================================================================================================
#CANDIDATOS
#Retorna todos os candidatos
def candidates(request):
    all_candidates = PersonalData.objects.all()
    template = loader.get_template("recrutamento/candidates/candidatos.html")
    context = { 
        "all_candidates": all_candidates,
    }
    return HttpResponse(template.render(context, request))

#Retorna um candidato baseado em seu Id
def single_candidate(request, candidate_id):
    specific_candidate = get_object_or_404(PersonalData, pk=candidate_id)
    return render(request, "recrutamento/candidates/singlecandidato.html", {"specific_candidate": specific_candidate})

def post_candidate(request):
    if request.method == 'POST':
        form = FormularioPersonalData(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Candidato criado com sucesso!")
    else:
        form = FormularioPersonalData()
    return render(request, 'recrutamento/candidates/add_candidate.html', {'form': form})

#Deleta candidato baseado em seu Id
def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(PersonalData, pk=candidate_id)
    candidate.delete()
    return HttpResponse("Candidato deletado com sucesso!")

def confirm_delete_candidate(request, candidate_id):
    candidate_to_delete = get_object_or_404(PersonalData, pk=candidate_id)
    return render(request, 'recrutamento/candidates/confirm_delete_candidate.html', {'candidate_to_delete': candidate_to_delete})

def update_candidate(request, candidate_id):
    candidate = get_object_or_404(PersonalData, pk=candidate_id)

    if request.method == 'POST':
        form = FormularioPersonalData(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidates')

    else:
        form = FormularioPersonalData(instance=candidate)

    return render(request, 'recrutamento/candidates/edit_candidate.html', {'form': form, 'candidate': candidate})
#====================================================================================================================================================================
#CONTATO
#Retorna todos os contatos
def contacts(request):
    all_contacts = Contact.objects.all()
    #all_candidates = PersonalData.objects.all()
    template = loader.get_template("recrutamento/contacts/contatos.html")
    context = {
        "all_contacts": all_contacts,
        #"all_candidates": all_candidates,
    }
    
    return HttpResponse(template.render(context, request))

#Retorna contato em especifico
def single_contact(request, contact_id):
    specific_contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, "recrutamento/contacts/singlecontact.html", {"specific_contact": specific_contact,})

#Cria contato
def post_contact(request):
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contato criado com sucesso!")
    else: 
        form = FormularioContato()
    return render(request, 'recrutamento/contacts/add_contact.html', {'form': form})

def confirm_delete_contact(request, contact_id):
    contact_to_delete = get_object_or_404(Contact, pk=contact_id)

    return render(request, 'recrutamento/contacts/confirm_delete_contact.html', {'contact_to_delete': contact_to_delete})    

def delete_contact(request, contact_id):

    if request.method == 'POST':
        contact_to_delete = get_object_or_404(Contact, pk=contact_id)
        contact_to_delete.delete()
        return redirect('contacts')

def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        form = FormularioContato(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts')

    else:
        form = FormularioContato(instance=contact)

    return render(request, 'recrutamento/contacts/edit_contact.html', {'form': form, 'contact': contact})

#====================================================================================================================================================================
#EXPERIENCIA PROFISSIONAL
def professional_experiences(request):
    all_professional_experiences = ProfessionalExperience.objects.all()
    template = loader.get_template("recrutamento/professional_experiences/all_professional_experiences.html")
    context = {
        "all_professional_experiences": all_professional_experiences,
    }
    return HttpResponse(template.render(context, request))

def single_professional_experience(request, professional_experience_id):
    specific_professional_experience = get_object_or_404(ProfessionalExperience, pk=professional_experience_id)
    return render(request, "recrutamento/professional_experiences/singleprofessionalexperience.html", {"specific_professional_experience": specific_professional_experience})

def post_professional_experience(request):
    if request.method == 'POST':
        form = FormularioProfessionalExperience(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Experiência profissional criada com sucesso!")
    else:
        form = FormularioProfessionalExperience()
    return render(request, 'recrutamento/professional_experiences/add_professional_experience.html', {'form': form})

def update_professional_experience(request, professional_experience_id):
    professional_experience = get_object_or_404(ProfessionalExperience, pk=professional_experience_id)
    
    if request.method == 'POST':
        form = FormularioProfessionalExperience(request.POST, instance=professional_experience)
        if form.is_valid():
            form.save()
            return redirect('professional_experiences')
    else:
        form = FormularioProfessionalExperience(instance=professional_experience)
    return render(request, "recrutamento/professional_experiences/edit_professional_experience.html", {'form': form, 'professional_experience': professional_experience})

def confirm_delete_professional_experience(request, professional_experience_id):
    professional_experience_to_delete = get_object_or_404(ProfessionalExperience, pk=professional_experience_id)

    return render(request, 'recrutamento/professional_experiences/confirm_delete_professional_experience.html', {'professional_experience_to_delete': professional_experience_to_delete},)    


def delete_professional_experience(request, professional_experience_id):
    if request.method == 'POST':
        professional_experience_to_delete = get_object_or_404(ProfessionalExperience, pk=professional_experience_id)
        professional_experience_to_delete.delete()
        return redirect('professional_experiences')
#====================================================================================================================================================================
#FORMAÇÃO ACADEMICA
def academic_formations(request):
    all_academic_formations = AcademicFormation.objects.all()
    template = loader.get_template("recrutamento/academic_formations/academic_formations.html")
    context = {
        "all_academic_formations": all_academic_formations,
    }
    return HttpResponse(template.render(context, request))

def single_academic_formation(request, academic_formation_id):
    specific_academic_formation = get_object_or_404(AcademicFormation, pk=academic_formation_id)
    return render(request, "recrutamento/academic_formations/singleacademicformation.html", {"specific_academic_formation": specific_academic_formation})

def post_academic_formation(request):
    if request.method == 'POST':
        form = FormularioAcademicFormation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Formação acadêmica registrada com sucesso!")
    else:
        form = FormularioAcademicFormation()
    return render(request, 'recrutamento/academic_formations/add_academic_formation.html', {'form': form})

def update_academic_formation(request, academic_formation_id):
    academic_formation = get_object_or_404(AcademicFormation, pk=academic_formation_id)
    if request.method == 'POST':
        form = FormularioAcademicFormation(request.POST, instance=academic_formation)
        if form.is_valid():
            form.save()
            return redirect('academic_formations')
    else:
        form = FormularioAcademicFormation(instance=academic_formation)
    return render(request, "recrutamento/academic_formations/edit_academic_formation.html", {'form': form, 'academic_formation': academic_formation})

def confirm_delete_academic_formation(request, academic_formation_id):
    academic_formation_to_delete = get_object_or_404(AcademicFormation, pk=academic_formation_id)

    return render(request, 'recrutamento/academic_formations/confirm_delete_academic_formation.html', {'academic_formation_to_delete': academic_formation_to_delete},)

def delete_academic_formation(request, academic_formation_id):
    if request.method == 'POST':
        academic_formation_to_delete = get_object_or_404(AcademicFormation, pk=academic_formation_id)
        academic_formation_to_delete.delete()
        return redirect('academic_formations')
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

    return render(request, 'recrutamento/curriculums/send_application.html', {
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
    return render(request, 'recrutamento/curriculums/single_curriculum.html', context)

#Pega todos os curriculos
def get_all_curriculums(request):
    curriculos = Curriculo.objects.all()
    context = {
        'curriculos': curriculos,
    }
    return render(request, 'recrutamento/curriculums/all_curriculums.html', context)

def confirm_delete_curriculum(request, curriculum_id):
    curriculum_to_delete = get_object_or_404(Curriculo, pk=curriculum_id)

    return render(request, 'recrutamento/curriculums/confirm_delete.html', {'curriculum_to_delete': curriculum_to_delete})    
   
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

    return render(request, 'recrutamento/curriculums/edit_curriculum.html', {
        'personal_data_form': personal_data_form,
        'contact_form': contact_form,
        'professional_experience_form': professional_experience_form,
        'academic_formation_form': academic_formation_form,
        'curriculo': curriculo,  # Adicione para usar na exibição se necessário
    })