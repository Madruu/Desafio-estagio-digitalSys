from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidate/<int:candidate_id>", views.single_candidate, name="single_candidate"),
    path("send/", views.post_curriculos, name="post_curriculos"),
]