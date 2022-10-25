import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import LoginForm, DesignForm
from .models import Design


def design_list(request):
    designs = Design.objects.all()
    return render(request, 'mockup/design_list.html', {'designs': designs})

def design(request):
    designs = Design.objects.all()
    return render(request, 'mockup/design.html', {'designs': designs})

# def create(request):
#     return render(request, 'mockup/create.html')


# Design SHOW
def created_design(request, pk):
    design = Design.objects.get(id=pk)
    return render(request, 'mockup/created_design.html', {'design': design})

# Create a new design
def create(request):
    designs = Design.objects.all()
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        print("LINE 61")
        if form.is_valid():
            print("LINE 63")
            print(request.user)
            design = form.save(commit=False)
            design.user = request.user
            print(design.user)
            # title = form.cleaned_data['title']
            # print(title)
            # design.save()
            design = form.save()
            print("LINE 65")
            return render(request, 'mockup/design_list.html', {'designs': designs})
    else:
        form = DesignForm()
    return render(request, 'mockup/create.html', {'form': form})

# Image File Upload to Database
# @require_POST
# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     document = Document.objects.create(document=path, upload_by=request.user)
#     return JsonResponse({'document': document.id})

