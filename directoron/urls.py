from django.urls import path

from . import views

app_name = "directoron"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("<int:question_id>/", views.detail, name="detail"),
]
