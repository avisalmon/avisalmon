from django.shortcuts import render, get_object_or_404
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/portfolio.html', context)

def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {'project': project}
    return render(request, 'portfolio/project_details.html', context)
