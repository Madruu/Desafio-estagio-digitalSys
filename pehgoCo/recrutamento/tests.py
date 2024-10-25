"""from django.test import TestCase
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation

# Create your tests here.
class PersonalDataTest(TestCase):
    def test_personal_data(self):
        personal_data = PersonalData.objects.create(
            first_name='Joao', 
            last_name='Oliveira', 
            birth_date='1998-01-01',
            personal_doc='527.873.528-71'
        )	
        self.assertEqual(str(personal_data), 'Joao Oliveira 1998-01-01 527.873.528-71')
    
        self.assertTrue(isinstance(personal_data, PersonalData))
        
class ContactTest(TestCase):
    def test_contact(self):
        contact = Contact.objects.create(
            email='vitordtulio@gmail.com',
            phone_number='14991341794',
            rua='Rua 1',
            bairro='Bairro 1',
            cidade='Cidade 1',
            estado='SP',
            cep='12345678',
            complemento='Casa'
        )
        self.assertEqual(str(contact), 'vitordtulio@gmail.com 14991341794 Rua 1 Bairro 1 Cidade 1 SP 12345678 Casa')

class ProfessionalExperienceTest(TestCase):
    def test_professional_experience(self):
        professional_experience = ProfessionalExperience.objects.create(
            cargo='Desenvolvedor',
            empresa='DigitalSys',
            periodo=2,
            description='Desenvolvimento de sistemas'
        )
        self.assertEqual(str(professional_experience), 'Desenvolvedor DigitalSys 2 Desenvolvimento de sistemas')

class AcademicFormationTest(TestCase):
    def test_academic_formation(self):
        academic_formation = AcademicFormation.objects.create(
            institution='Fatec',
            curse='ADS',
            stage=5
        )
        self.assertEqual(str(academic_formation), 'Fatec ADS 1')"""