from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project


projectslist = [
    {
        'id': '1',
        'title': 'Project 1',
        'description': 'This is the first project',
    },
    {
        'id': '2',
        'title': 'Project 2',
        'description': 'This is the second project',
    },
    {
        'id': '3',
        'title': 'Project 3',
        'description': 'This is the third project',
    },
]


def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    return render(request, 'projects/single-project.html', {
        'project': projectObj,
        'tags': tags
    })