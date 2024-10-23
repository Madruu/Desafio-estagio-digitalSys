from django import forms
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation, Curriculo
from phonenumber_field.formfields import PhoneNumberField

class FormularioPersonalData(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
    class Meta:
        model = PersonalData
        fields = ['first_name', 'last_name', 'birth_date', 'personal_doc']

class FormularioContato(forms.ModelForm):
    phone_number = PhoneNumberField(region="BR")
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
        
        
class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = [] 