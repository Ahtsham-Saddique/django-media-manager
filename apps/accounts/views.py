
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import student

def  home(request):

    return render(request,'base.html')

def  login(request):

    return render(request,'login.html')
def  students(request):
    students=student.objects.all()
    return render(request,'students.html',{'students': students })

def  add_student(request):
    if request.method=='POST':
        Name= request.POST.get('name')
        Age= request.POST.get('age')
        Gender= request.POST.get('gender')
        email= request.POST.get('email')
        image= request.FILES.get('image')
        Branch= request.POST.get('branch')

        Student=student(
            name = Name ,
            age= Age ,
            gender= Gender ,
            email= email ,
            image=image ,
            branch = Branch


        )
        Student.save()
        return redirect('students')
    return render(request,'add_student.html')

def update_student(request,id):
    student_obj = student.objects.filter(id=id).first()
    if request.method=='POST':
        Name= request.POST.get('name')
        Age= request.POST.get('age')
        Gender= request.POST.get('gender')
        email= request.POST.get('email')
        image= request.FILES.get('image')
        Branch= request.POST.get('branch')

        student_obj.age=Age
        student_obj.gender=Gender
        student_obj.name=Name
        student_obj.email=email
        if image:
            student_obj.image=image
        student_obj.branch=Branch

        student_obj.save()
        return redirect(students)

    return render (request,'update_student.html',{'student':student_obj})

def delete_student(request,id):
    
    student_obj = student.objects.filter(id=id).first()
    student_obj.delete()
    return render(request,'delete_student.html',{'student':student_obj})
