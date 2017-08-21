from django.shortcuts import render, redirect

def project(request):
    return redirect('proj_doing')

def proj_doing(request):
    return render(request, 'project/proj_doing.html', {})

def proj_done(request):
    return render(request, 'project/proj_done.html', {})
