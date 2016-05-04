from django.shortcuts import render

# Create your views here.

from .import forms
from .models import Message
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# the view is returning data via a post request,
# so make it pay attention to the request method.
def contact_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        # handle data accordingly from post variable.
        form = forms.ContactForm(request.POST)
        # check if the form is valid.
        if form.is_valid():
            print("Good form")
            print("Data dump :")

            # access data with form.cleaned_data['key_name']
            name  = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message_text']

            # now put the data into the database
            db_entry = Message()
            db_entry.name = name
            db_entry.email = email
            db_entry.message_text = message_text

            # save the message
            db_entry.save()


    return render(request, 'contact/contact_form.html', {'form':form})
