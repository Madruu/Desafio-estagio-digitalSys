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


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def authenticate(request, format=None):
    content ={
        'user': str(request.user),
        'auth': str(request.auth),
    }
    
    return Response(content)


@api_view(['GET'])
def get_data_personal_data(request):
    personal_datas = PersonalData.objects.all()
    serializer = PersonalDataSerializer(personal_datas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_single_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonalDataSerializer(personal_data)
    
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_data_personal_data(request):
    serializer = PersonalDataSerializer(data=request.data)
    if serializer.is_valid():
        # Tente adicionar um log para depuração
        print("Saving the data...")  # Isso aparecerá no console durante a requisição
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def update_data_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonalDataSerializer(personal_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_data_personal_data(request, id):
    try:
        personal_data = PersonalData.objects.get(pk=id)
    except PersonalData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    personal_data.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

#====================================================================================================================================================================
#CONTACT VIEWS
@api_view(['GET'])
def get_data_contact(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_single_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(contact)
    
    return Response(serializer.data)    
    

@api_view(['GET', 'POST'])
def post_data_contact(request):
    serializer = ContactSerializer (data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT'])
def update_data_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(contact, data=request.data, partial=True)
    
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'DELETE'])
def delete_data_contact(request, id):
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    contact.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#====================================================================================================================================================================
#PROFESSIONAL EXPERIENCE VIEWS
@api_view(['GET'])
def get_data_professional_experience(request):
    professional_experience = ProfessionalExperience.objects.all()
    serializer = ProfessionalExperienceSerializer(professional_experience, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_single_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfessionalExperienceSerializer(professional_experience)
    
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_data_professional_experience(request):
    serializer = ProfessionalExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def update_data_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfessionalExperienceSerializer(professional_experience, data=request.data, partial=True)
    
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_data_professional_experience(request, id):
    try:
        professional_experience = ProfessionalExperience.objects.get(pk=id)
    except ProfessionalExperience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    professional_experience.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

#====================================================================================================================================================================
#ACADEMIC FORMATION VIEWS
@api_view(['GET'])
def get_data_academic_formation(request):
    academic_formation  = AcademicFormation.objects.all()
    serializer = AcademicFormationSerializer(academic_formation, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_single_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AcademicFormationSerializer(academic_formation)
    
    
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_data_academic_formation(request):
    serializer = AcademicFormationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def update_data_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AcademicFormationSerializer(academic_formation, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_data_academic_formation(request, id):
    try:
        academic_formation = AcademicFormation.objects.get(pk=id)
    except AcademicFormation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    academic_formation.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

#====================================================================================================================================================================
#CURRICULUM VIEWS
@api_view(['GET'])
def get_data_curriculo(request):
    curriculos = Curriculo.objects.all()
    serializer = CurriculoSerializer(curriculos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_data_single_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)
    except Curriculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CurriculoSerializer(curriculo)
    
    return Response(serializer.data)    
        

@api_view(['GET', 'POST'])
def post_data_curriculo(request):
    print("DADOS", request.data)
    serializer = CurriculoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def update_data_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)
    except Curriculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CurriculoSerializer(curriculo, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def delete_data_curriculo(request, id):
    try:
        curriculo = Curriculo.objects.get(pk=id)
    except Curriculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    curriculo.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)