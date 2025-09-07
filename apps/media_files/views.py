from django.shortcuts import render
from .models import Upload
# Create your views here.
def upload(request):

    if request.method == "POST":
        file_name=request.POST.get("file_name")   
        upload_file=request.FILES.get("upload_file")

        Upload.objects.create( file_name = file_name,
                              upload_file = upload_file,
                              )
    uploads=Upload.objects.all()
    return render(request,"upload.html",{"uploads":uploads})