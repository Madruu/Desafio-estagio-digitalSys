from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from recrutamento.models import Curriculo, PersonalData, Contact, ProfessionalExperience, AcademicFormation
from .serializers import PersonalDataSerializer, ContactSerializer, ProfessionalExperienceSerializer, AcademicFormationSerializer, CurriculoSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#====================================================================================================================================================================
# PERSONAL DATA VIEWS
def index(request):
    return HttpResponse("Este será o sistema de candidatos usando api")

#Retorna o usuário autenticado
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def authenticate(request, format=None):
    content ={
        'user': str(request.user),
        'auth': str(request.auth),
    }
    
    return Response(content)


#Retorna todos os dados de PersonalData
@api_view(['GET'])
def get_data_personal_data(request):
    personal_datas = PersonalData.objects.all()#Pega todos os dados de PersonalData
    serializer = PersonalDataSerializer(personal_datas, many=True)#Serializa os dados
    return Response(serializer.data)#Retorna os dados serializados

#Retorna um dado de PersonalData
@api_view(['GET'])
def get_data_single_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)#Pega um dado de PersonalData
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = PersonalDataSerializer(personal_data)#Serializa o dado
    
    return Response(serializer.data)#Retorna o dado serializado

#Adiciona um dado de PersonalData
@api_view(['GET', 'POST'])
def post_data_personal_data(request):
    serializer = PersonalDataSerializer(data=request.data)#Serializa os dados recebidos
    if serializer.is_valid():#Verifica se os dados são válidos
        serializer.save()#Salva os dados
        return Response(serializer.data, status=status.HTTP_201_CREATED)#Retorna os dados serializados
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'PUT'])
def update_data_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)#Pega um dado de PersonalData
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = PersonalDataSerializer(personal_data, data=request.data, partial=True)#Permite o preenchimento de apenas alguns campos, sem precisar inserir todos
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

#Deleta um dado de PersonalData
@api_view(['GET', 'DELETE'])
def delete_data_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)#Pega um dado de PersonalData
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    personal_data.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

#====================================================================================================================================================================
#CONTACT VIEWS
@api_view(['GET'])
def get_data_contact(request):
    contacts = Contact.objects.all()#Pega todos os dados de Contact
    serializer = ContactSerializer(contacts, many=True)#Serializa os dados
    return Response(serializer.data)#Retorna os dados serializados

@api_view(['GET'])
def get_data_single_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)#Pega um dado de Contact
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = ContactSerializer(contact)#Serializa o dado
    
    return Response(serializer.data)#Retorna o dado serializado
    
#Adiciona um dado de Contact
@api_view(['GET', 'POST'])
def post_data_contact(request):
    serializer = ContactSerializer (data=request.data)#Serializa os dados recebidos
    
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos
        
@api_view(['GET','PUT'])
def update_data_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)#Pega um dado de Contact
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = ContactSerializer(contact, data=request.data, partial=True)#Permite o preenchimento de apenas alguns campos, sem precisar inserir todos
    
    if(serializer.is_valid()):
        serializer.save()#Salva os dados
        return Response(serializer.data)#Retorna os dados serializados
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos
        
@api_view(['GET', 'DELETE'])
def delete_data_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)#Pega um dado de Contact
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    contact.delete()#Deleta o dado
    return Response(status=status.HTTP_204_NO_CONTENT)#Retorna status 204

#====================================================================================================================================================================
#PROFESSIONAL EXPERIENCE VIEWS
@api_view(['GET'])
def get_data_professional_experience(request):
    professional_experience = ProfessionalExperience.objects.all()#Pega todos os dados de ProfessionalExperience
    serializer = ProfessionalExperienceSerializer(professional_experience, many=True)#Serializa os dados
    return Response(serializer.data)#Retorna os dados serializados

@api_view(['GET'])
def get_data_single_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)#Pega um dado de ProfessionalExperience
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = ProfessionalExperienceSerializer(professional_experience)#Serializa o dado
    
    return Response(serializer.data)#Retorna o dado serializado

@api_view(['GET', 'POST'])
def post_data_professional_experience(request):
    serializer = ProfessionalExperienceSerializer(data=request.data)#Serializa os dados recebidos
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data, status=status.HTTP_201_CREATED)#Retorna os dados serializados
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'PUT'])
def update_data_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)#Pega um dado de ProfessionalExperience
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = ProfessionalExperienceSerializer(professional_experience, data=request.data, partial=True)#Permite o preenchimento de apenas alguns campos, sem precisar inserir todos
    
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)#Retorna os dados serializados
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_data_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)#Pega um dado de ProfessionalExperience
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    professional_experience.delete()#Deleta o dado
    
    return Response(status=status.HTTP_204_NO_CONTENT)#Retorna status 204

#====================================================================================================================================================================
#ACADEMIC FORMATION VIEWS
@api_view(['GET'])
def get_data_academic_formation(request):
    academic_formation  = AcademicFormation.objects.all()#Pega todos os dados de AcademicFormation
    serializer = AcademicFormationSerializer(academic_formation, many=True)#Serializa os dados
    return Response(serializer.data)#Retorna os dados serializados

@api_view(['GET'])
def get_data_single_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)#Pega um dado de AcademicFormation
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = AcademicFormationSerializer(academic_formation)#Serializa o dado
    
    
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_data_academic_formation(request):
    serializer = AcademicFormationSerializer(data=request.data)#Serializa os dados recebidos
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)#Retorna os dados serializados
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'PUT'])
def update_data_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)#Pega um dado de AcademicFormation
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = AcademicFormationSerializer(academic_formation, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data)#Retorna os dados serializados
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'DELETE'])
def delete_data_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)#Pega um dado de AcademicFormation
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    academic_formation.delete()#Deleta o dado
    
    return Response(status=status.HTTP_204_NO_CONTENT)#Retorna status 204

#====================================================================================================================================================================
#CURRICULUM VIEWS
@api_view(['GET'])
def get_data_curriculo(request):
    curriculos = Curriculo.objects.all()#Pega todos os dados de Curriculo
    serializer = CurriculoSerializer(curriculos, many=True)#Serializa os dados
    return Response(serializer.data)#Retorna os dados serializados

@api_view(['GET'])
def get_data_single_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)#Pega um dado de Curriculo
    except Curriculo.DoesNotExist:#Retorna erro 404 caso não encontre o dado
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CurriculoSerializer(curriculo)#Serializa o dado
    
    return Response(serializer.data)#Retorna o dado serializado
        

@api_view(['GET', 'POST'])
def post_data_curriculo(request):
    print("DADOS", request.data)#Imprime os dados recebidos
    serializer = CurriculoSerializer(data=request.data)#Serializa os dados recebidos
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data, status=status.HTTP_201_CREATED)#Retorna os dados serializados
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'PUT'])
def update_data_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)#Pega um dado de Curriculo
    except Curriculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    serializer = CurriculoSerializer(curriculo, data=request.data, partial=True)#Permite o preenchimento de apenas alguns campos, sem precisar inserir todos
    if serializer.is_valid():
        serializer.save()#Salva os dados
        return Response(serializer.data)#Retorna os dados serializados
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Retorna erro 400 caso os dados não sejam válidos

@api_view(['GET', 'DELETE'])
def delete_data_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)#Pega um dado de Curriculo
    except Curriculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Retorna erro 404 caso não encontre o dado
    
    curriculo.delete()#Deleta o dado
    
    return Response(status=status.HTTP_204_NO_CONTENT)#Retorna status 204