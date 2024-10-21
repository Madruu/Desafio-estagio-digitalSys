from django import forms
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation, Curriculo

class FormularioPersonalData(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )
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
        
        
class CurriculumForm(forms.Form):
    personal_data = FormularioPersonalData()
    contact = FormularioContato()
    professional_experience = FormularioProfessionalExperience()
    academic_formation = FormularioAcademicFormation()

    #wargs = keyword arguments 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicializar subformularios com os dados POST se houver
        if args:
            self.fields['personal_data'] = FormularioPersonalData(args[0])
            self.fields['contact'] = FormularioContato(args[0])
            self.fields['professional_experience'] = FormularioProfessionalExperience(args[0])
            self.fields['academic_formation'] = FormularioAcademicFormation(args[0])

    def is_valid(self):
        # Verifica se todos os subformularios sao validos
        return (self.fields['personal_data'].is_valid() and
                self.fields['contact'].is_valid() and
                self.fields['professional_experience'].is_valid() and
                self.fields['academic_formation'].is_valid())

    def save(self):
        # Salva cada um dos subformularios
        personal_data = self.fields['personal_data'].save()
        contact = self.fields['contact'].save()
        professional_experience = self.fields['professional_experience'].save()
        academic_formation = self.fields['academic_formation'].save()

        # Cria e salva o Curriculo com os dados salvos dos subformularios
        curriculo = Curriculo(
            curr_personal_data=personal_data,
            curr_contact=contact,
            curr_professional_experience=professional_experience,
            curr_academic_formation=academic_formation
        )
        curriculo.save()

