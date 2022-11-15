from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def all_contact(request):
    """ A view to show all contact us submissions """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = Contact.objects.all()

    context = {
        'contact' : contact,
    }
    
    return render(request, 'contact/contact.html', context)


@login_required
def contact_detail(request, contact_id):
    """ A view to show contact detail """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact' : contact,
    }
    
    return render(request, 'contact/contact_detail.html', context)


@login_required
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


@login_required
def delete_contact(request, contact_id):
    """ Delete an order detail from the submitted details """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Order Details Deleted!')
    return redirect(reverse('contacts'))
