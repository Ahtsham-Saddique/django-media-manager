from django.shortcuts import render,redirect
from .forms import mform
from.models import Media

# Create your views here.
def media(request):
    

    if request.method== "post":
        form= mform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('students')

    else:
        form=mform()

    file=Media.objects.all()

    context={
        'form':form,
        'file':file,


    }
    return render(request,'media_apps.html',
                  context)