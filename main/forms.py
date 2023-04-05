# from django import forms
from django import forms
from main.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','phone_number','address','message','country','university','course']
