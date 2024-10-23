from django.urls import path

from projects.views import projects, project, createProject

urlpatterns = [
    path('', projects, name="projects"),
    path('project/<str:pk>', project, name="project"),
    path('create-project/', createProject, name="create-project"),
]