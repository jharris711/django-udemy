from django.db.models import Q

from users.models import Profile, Skill


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(
        name__icontains=search_query
    )

    profile = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(headline__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profile, search_query
