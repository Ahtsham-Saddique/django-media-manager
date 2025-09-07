from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.
def home(request):
    formm = Contact.objects.all()
    if request.method =="POST":
        
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
    
        form=ContactForm()
    context = {
        'form' : form,
        'formm' : formm,
    }
    
    return render(request,'contact.html',context)