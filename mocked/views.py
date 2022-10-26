
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
            design = form.save()
            print("LINE 65")
            return render(request, 'mocked/design_list.html', {'designs': designs})
    else:
        form = DesignForm()
    return render(request, 'mocked/create.html', {'form': form})