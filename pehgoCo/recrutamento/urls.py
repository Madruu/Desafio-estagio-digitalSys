from django.urls import path
from . import views


urlpatterns = [
    #Candidatos
    path("", views.index, name="index"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidates/add/", views.post_candidate, name="post_candidate"),
    path("candidate/<int:candidate_id>", views.single_candidate, name="single_candidate"),
    path("candidate/delete/<int:candidate_id>", views.delete_candidate, name="delete_candidate"),
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
    #Curriculos
    path("send/", views.post_curriculos, name="post_curriculos"),
    path("curriculums/", views.get_all_curriculums, name="get_all_curriculums"),
    path("curriculum/<int:curriculum_id>", views.get_single_curriculum, name="get_single_curriculum"),
    path("curriculum/delete/<int:curriculum_id>", views.delete_curriculum, name="delete_curriculum"),
    path("curriculum/delete/confirm/<int:curriculum_id>", views.confirm_delete_curriculum, name="confirm_delete_curriculum"),
    path("curriculum/edit/<int:curriculum_id>", views.update_curriculum, name="update_curriculum"),
]