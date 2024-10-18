from django import forms
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation

class FormularioPersonalData(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = ['first_name', 'last_name', 'birth_date', 'personal_doc']

class FormularioContato(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'phone_number', 'rua', 'bairro', 'cidade', 'estado', 'cep', 'complemento']
        
class FormularioProfessionalExperience(forms.ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = ['cargo', 'empresa', 'periodo', 'description']
        
class FormularioAcademicFormation(forms.ModelForm):
    class Meta:
        model = AcademicFormation
        fields = ['institution', 'curse', 'stage']