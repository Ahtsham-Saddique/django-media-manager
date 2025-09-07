from django import forms
from .models import Media
class mform(forms.ModelForm):
    class Meta:
        model=Media
        fields=['File_Name','Upload_File']


        