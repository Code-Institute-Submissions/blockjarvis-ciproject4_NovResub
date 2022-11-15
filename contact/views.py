from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

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


def add_contact(request):
    """ Add an order details  """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added order details!')
            return redirect(reverse('add_contact'))
        else:
            messages.error(request, 'Failed to add order details. Please ensure the form is valid.')
    else:    
        form = ContactForm()

    template = 'contact/add_contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
