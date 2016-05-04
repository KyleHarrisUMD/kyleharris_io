from django.shortcuts import render

# Create your views here.

from .import forms

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
    return render(request, 'contact/contact_form.html', {'form':form})
