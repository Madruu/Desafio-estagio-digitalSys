from django.urls import path
from . import views


urlpatterns = [
     path('favicon.ico', views.favicon_view, name='favicon_view'),
    #Candidatos
    path("", views.index, name="index"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidates/add/", views.post_candidate, name="post_candidate"),
    path("candidate/<int:candidate_id>", views.single_candidate, name="single_candidate"),
    path("candidate/delete/<int:candidate_id>", views.delete_candidate, name="delete_candidate"),
    path("candidate/delete/confirm/<int:candidate_id>", views.confirm_delete_candidate, name="confirm_delete_candidate"),
    path("candidate/edit/<int:candidate_id>", views.update_candidate, name="update_candidate"),
    #Contactos
    path("contatos/", views.contacts, name="contacts"),
    path("contato/<int:contact_id>", views.single_contact, name="single_contact"),
    path("contatos/add/", views.post_contact, name="post_contact"),
    path("contato/delete/<int:contact_id>", views.delete_contact, name="delete_contact"),
    path("contato/delete/confirm/<int:contact_id>", views.confirm_delete_contact, name="confirm_delete_contact"),
    path("contato/edit/<int:contact_id>", views.update_contact, name="update_contact"),
    #Experiencia Profissional
    path("professional_experiences/", views.professional_experiences, name="professional_experiences"),
    path("professional_experience/<int:professional_experience_id>", views.single_professional_experience, name="single_professional_experience"),
    path("professional_experience/add/" , views.post_professional_experience, name="post_professional_experience"),
    path("professional_experience/edit/<int:professional_experience_id>" , views.update_professional_experience, name="update_professional_experience"),
    path("professional_experience/delete/<int:professional_experience_id>", views.delete_professional_experience, name="delete_professional_experience"),
    path("professional_experience/delete/confirm/<int:professional_experience_id>", views.confirm_delete_professional_experience, name="confirm_delete_professional_experience"),
    #Formação academica
    path("academic_formations/", views.academic_formations, name="academic_formations"),
    path("academic_formation/<int:academic_formation_id>", views.single_academic_formation, name="single_academic_formation"),
    path("academic_formation/add/", views.post_academic_formation, name="post_academic_formation"),
    path("academic_formation/edit/<int:academic_formation_id>", views.update_academic_formation, name="update_academic_formation"),
    path("academic_formation/delete/<int:academic_formation_id>", views.delete_academic_formation, name="delete_academic_formation"),
    path("academic_formation/delete/confirm/<int:academic_formation_id>", views.confirm_delete_academic_formation, name="confirm_delete_academic_formation"),
    #Curriculos
    path("send/", views.post_curriculos, name="post_curriculos"),
    path("curriculums/", views.get_all_curriculums, name="get_all_curriculums"),
    path("curriculum/<int:curriculum_id>", views.get_single_curriculum, name="get_single_curriculum"),
    path("curriculum/delete/<int:curriculum_id>", views.delete_curriculum, name="delete_curriculum"),
    path("curriculum/delete/confirm/<int:curriculum_id>", views.confirm_delete_curriculum, name="confirm_delete_curriculum"),
    path("curriculum/edit/<int:curriculum_id>", views.update_curriculum, name="update_curriculum"),
]