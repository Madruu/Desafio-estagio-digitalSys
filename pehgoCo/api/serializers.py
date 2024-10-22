from rest_framework import serializers
from recrutamento.models import Curriculo, PersonalData, Contact, ProfessionalExperience, AcademicFormation

class PersonalDataSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(input_formats=["%d/%m/%Y"])
    
    class Meta:
        model = PersonalData
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'
        
class AcademicFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicFormation
        fields = '__all__'
        
class CurriculoSerializer(serializers.ModelSerializer):
    curr_personal_data = PersonalDataSerializer()
    curr_contact = ContactSerializer()
    curr_professional_experience = ProfessionalExperienceSerializer()
    curr_academic_formation = AcademicFormationSerializer()

    class Meta:
        model = Curriculo
        fields = ['id', 'curr_personal_data', 'curr_contact', 'curr_professional_experience', 'curr_academic_formation']

    def create(self, validated_data):
        personal_data_data = validated_data.pop('curr_personal_data')
        contact_data = validated_data.pop('curr_contact')
        professional_experience_data = validated_data.pop('curr_professional_experience')
        academic_formation_data = validated_data.pop('curr_academic_formation')

        curr_personal_data = PersonalData.objects.create(**personal_data_data)
        curr_contact = Contact.objects.create(**contact_data)
        curr_professional_experience = ProfessionalExperience.objects.create(**professional_experience_data)
        curr_academic_formation = AcademicFormation.objects.create(**academic_formation_data)

        curriculo = Curriculo.objects.create(
            curr_personal_data=curr_personal_data,
            curr_contact=curr_contact,
            curr_professional_experience=curr_professional_experience,
            curr_academic_formation=curr_academic_formation,
            **validated_data
        )
        return curriculo
    
    def update(self, instance, validated_data):
    # Atualiza os dados pessoais
        personal_data = validated_data.pop('curr_personal_data', None)  # Usando 'curr_personal_data'
        if personal_data:
            for attr, value in personal_data.items():
                setattr(instance.curr_personal_data, attr, value)
            instance.curr_personal_data.save()

        # Atualiza o contato
        contact_data = validated_data.pop('curr_contact', None)
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.curr_contact, attr, value)
            instance.curr_contact.save()

    # Atualiza a experiência profissional
        experience_data = validated_data.pop('curr_professional_experience', None)
        if experience_data:
            for attr, value in experience_data.items():
                setattr(instance.curr_professional_experience, attr, value)
            instance.curr_professional_experience.save()

    # Atualiza a formação acadêmica
        academic_data = validated_data.pop('curr_academic_formation', None)
        if academic_data:
            for attr, value in academic_data.items():
                setattr(instance.curr_academic_formation, attr, value)
            instance.curr_academic_formation.save()

    # Atualiza qualquer outro campo do curriculo
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance