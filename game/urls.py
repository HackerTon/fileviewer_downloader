from django.urls import path

from . import views

app_name = "game"
urlpatterns = [
    path("", views.index, name="index"),
    path("view_files/", views.view_files, name="view_files"),
    path("download/<str:path>", views.download, name="download"),
]
