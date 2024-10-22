from django.shortcuts import render
from django.http import HttpResponse


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
    page = 'projects'
    number = 10
    context = {
        'page': page,
        'number': number,
        'projects': projectslist
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None

    for i in projectslist:
        if i['id'] == pk:
            projectObj = i

    return render(request, 'projects/single-project.html', {
        'project': projectObj
    })