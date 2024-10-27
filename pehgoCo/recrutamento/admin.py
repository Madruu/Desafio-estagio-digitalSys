from django.contrib import admin
from .models import PersonalData, Contact, ProfessionalExperience, AcademicFormation, Curriculo

# Register your models here.
admin.site.register(PersonalData)
admin.site.register(Contact)
admin.site.register(ProfessionalExperience)
admin.site.register(AcademicFormation)
admin.site.register(Curriculo)