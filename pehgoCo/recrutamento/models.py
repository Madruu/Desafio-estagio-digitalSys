from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

def validate_email(value):
    #Validação de email
    if not value.endswith('.com'):#Verifica se o email termina com .com
        raise ValidationError('O formato do email está incorreto. Por favor, insira um email válido.')


# Create your models here.
class PersonalData(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    personal_doc = models.CharField(max_length=14)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.personal_doc}'

class Contact(models.Model):
    email = models.EmailField(validators=[validate_email])#Validação de email
    phone_number = PhoneNumberField(blank=True)#validação de telefone
    #Endereço
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.email} {self.phone_number} {self.rua} {self.bairro} {self.cidade} {self.estado} {self.cep} {self.complemento}'
    
class ProfessionalExperience(models.Model):
    cargo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    periodo = models.IntegerField()
    description = models.CharField(max_length=200)
    def __str__(self):  
        return f'{self.cargo} {self.empresa} {self.periodo} {self.description}'

class AcademicFormation(models.Model):
    institution = models.CharField(max_length=200)
    curse = models.CharField(max_length=200)
    stage = models.IntegerField()
    def __str__(self):
        return f'{self.institution} {self.curse} {self.stage}'
    
class Curriculo(models.Model):
    curr_personal_data = models.OneToOneField(PersonalData, on_delete=models.CASCADE)
    curr_contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    curr_professional_experience = models.OneToOneField(ProfessionalExperience, on_delete=models.CASCADE)
    curr_academic_formation = models.OneToOneField(AcademicFormation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Curriculo de {self.curr_personal_data.first_name}"
    