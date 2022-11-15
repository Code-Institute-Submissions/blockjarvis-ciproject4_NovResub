from django.shortcuts import render
from .models import Contact

# Create your views here.


def all_contact(request):
    """ A view to show all contact us submissions """

    contact = Contact.objects.all()

    context = {
        'contact' : contact,
    }
    
    return render(request, 'contact/contact.html', context)

