from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from recrutamento.models import PersonalData, Contact, ProfessionalExperience, AcademicFormation 
# Create your tests here.

class PersonalDataTest(APITestCase):
    # Teste de criação de um objeto PersonalData
    def test_personal_data(self):
        response = self.client.get(reverse('get_data_personal_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PersonalData.objects.count(), 0)

class ContactTest(APITestCase):
    # Teste de criação de um objeto Contact
    def test_contact(self):
        response = self.client.get(reverse('get_data_contact'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 0)
        
class ProfessionalExperienceTest(APITestCase):
    # Teste de criação de um objeto ProfessionalExperience
    def test_professional_experience(self):
        response = self.client.get(reverse('get_data_professional_experience'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProfessionalExperience.objects.count(), 0)
        
class AcademicFormationTest(APITestCase):
    # Teste de criação de um objeto AcademicFormation
    def test_academic_formation(self):
        response = self.client.get(reverse('get_data_academic_formation'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AcademicFormation.objects.count(), 0)