from django.urls import path

from projects.views import projects, project, createProject, deleteProject, updateProject

urlpatterns = [
    path('', projects, name="projects"),
    path('<str:pk>', project, name="project"),
    path('create-project/', createProject, name="create-project"),
    path('update-project/<str:pk>', updateProject, name="update-project"),
    path('delete-project/<str:pk>', deleteProject, name="delete-project"),
]