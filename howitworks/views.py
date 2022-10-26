
from django.shortcuts import render


def howitwork(request):
    template = 'howitworks/howitwork.html'
    context = {}

    return render(request, template, context)
