from django import forms


# just like a model create a
# class for a form. The way you use
# the form is almost identical to creating
# a model
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length= 50,
        widget=forms.TextInput(attrs={'class': "input"}),
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': "input"}),
    )
    # represent as an html widget, just reference the class
    message_text = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}),
    )