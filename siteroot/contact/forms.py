from django import forms


# just like a model create a
# class for a form. The way you use
# the form is almost identical to creating
# a model
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # represent as an html widget, just reference the class
    message_text = forms.CharField(widget=forms.Textarea)