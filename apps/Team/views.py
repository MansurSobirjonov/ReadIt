from django.shortcuts import render
from .models import Employer


def team_view(request):

    members = Employer.objects.all()

    context = {
        'members': members
    }
    return render(request, 'about.html', context)