

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def  about(request):

    return HttpResponse("This is the about page.. ")


def  home(request):
    # title={'title':'djagno learners, 'user_name': 'mohsin'}
    title={'title':'djagno learners',
           'user_name':'mohsin',
           'languages':['python',"java","cpp"],
           'loggedin':True}
    return render(request,"index.html",title)

