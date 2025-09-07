from django import forms

from .models import Contact
# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=50,label='Name')
#     email=forms.EmailField(max_length=100)

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']

