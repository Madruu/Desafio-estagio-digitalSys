from django.urls import path
from . import views

urlpatterns = [
    #Personal Data urls
    path("", views.index, name="index"),
    path("personaldata/", views.get_data_personal_data, name="get_data_personal_data"),
    path("personaldata/<int:id>", views.get_data_single_personal_data, name="get_data_single_personal_data"),
    path("add/", views.post_data_personal_data, name="post_data_personal_data"),
    path("edit/<int:id>", views.update_data_personal_data, name="update_data_personal_data"),
    path("delete/<int:id>", views.delete_data_personal_data, name="delete_data_personal_data"),
    
    #Contact urls
    path("contacts/", views.get_data_contact, name="get_data_contact"),
    path("contacts/<int:id>", views.get_data_single_contact, name="get_data_single_contact"),
    path("contacts/add/", views.post_data_contact, name="post_data_contact"),
    path("contact/edit/<int:id>", views.update_data_contact, name="update_data_contact"),
    path("contact/delete/<int:id>", views.delete_data_contact, name="delete_data_contact"),
    
    #Professional Experience urls
    path("professional_experiences/", views.get_data_professional_experience, name="get_data_professional_experience"),
    path("professional_experiences/<int:id>", views.get_data_single_professional_experience, name="get_data_single_professional_experience"),
    path("professional_experiences/add/", views.post_data_professional_experience, name="post_data_professional_experience"),
    path("professional_experience/edit/<int:id>", views.update_data_professional_experience, name="update_data_professional_experience"),
    path("professional_experience/delete/<int:id>", views.delete_data_professional_experience, name="delete_data_professional_experience"),
    
    #Academic Formation urls
    path("academic_formations/", views.get_data_academic_formation, name="get_data_academic_formation"),
    path("academic_formations/<int:id>", views.get_data_single_academic_formation, name="get_data_single_academic_formation"),
    path("academic_formations/add/", views.post_data_academic_formation, name="post_data_academic_formation"),
    path("academic_formation/edit/<int:id>", views.update_data_academic_formation, name="update_data_academic_formation"),
    path("academic_formation/delete/<int:id>", views.delete_data_academic_formation, name="delete_data_academic_formation"),
    
    #Curriculum urls
    path("curriculums/", views.get_data_curriculo, name="get_data_curriculum"),
    path("curriculums/<int:id>", views.get_data_single_curriculo, name="get_data_single_curriculum"),
    path("curriculums/add/", views.post_data_curriculo, name="post_data_curriculum"),
    path("curriculum/edit/<int:id>", views.update_data_curriculo, name="update_data_curriculum"),
    path("curriculum/delete/<int:id>", views.delete_data_curriculo, name="delete_data_curriculum"),
]