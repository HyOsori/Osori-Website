from django.shortcuts import render, redirect
from .models import Project

def project(request):
    return redirect('proj_doing')

def proj_doing(request):
    projects = Project.objects.filter(end_period__isnull=True).order_by('start_period')
    return render(request, 'project/proj_doing.html', {'projects': projects})

def proj_done(request):
    projects = Project.objects.filter(end_period__isnull=False).order_by('start_period')
    return render(request, 'project/proj_done.html', {'projects': projects})
