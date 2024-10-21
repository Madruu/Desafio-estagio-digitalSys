from django.urls import path
from . import views


urlpatterns = [
    #Candidatos
    path("", views.index, name="index"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidate/<int:candidate_id>", views.single_candidate, name="single_candidate"),
    path("candidate/delete/<int:candidate_id>", views.delete_candidate, name="delete_candidate"),
    #Curriculos
    path("send/", views.post_curriculos, name="post_curriculos"),
    #path("curriculums/", views.get_all_curriculums, name="get_all_curriculums"),
    path("curriculums/", views.get_all_curriculums, name="get_all_curriculums"),
    path("curriculum/<int:curriculum_id>", views.get_single_curriculum, name="get_single_curriculum"),
    path("curriculum/delete/<int:curriculum_id>", views.delete_curriculum, name="delete_curriculum"),
    path("curriculum/delete/confirm/<int:curriculum_id>", views.confirm_delete_curriculum, name="confirm_delete_curriculum"),
    path("curriculum/edit/<int:curriculum_id>", views.edit_curriculum, name="edit_curriculum"),
]