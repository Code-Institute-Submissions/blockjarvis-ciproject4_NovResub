from django.shortcuts import render, get_object_or_404
from .models import Contact

# Create your views here.


def all_contact(request):
    """ A view to show all contact us submissions """

    contact = Contact.objects.all()

    context = {
        'contact' : contact,
    }
    
    return render(request, 'contact/contact.html', context)


def contact_detail(request, contact_id):
    """ A view to show contact detail """

    contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact' : contact,
    }
    
    return render(request, 'contact/contact_detail.html', context)
