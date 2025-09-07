from django.db import models

# Create your models here.
class student(models.Model):

    slc_gender = [
        ('M','Male'),
        ('F','FeMale'),
        ('O','Others'),
        ]
    
    Branch = [
         ('CS','Computer Science'),
         ('AI',"Airtificial Intelligence"),
         ('ML','Machine learning')
         ]
 

    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=slc_gender,default='M')
    email=models.EmailField(unique=True)
    branch=models.CharField(max_length=50,choices=Branch)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.get_branch_display()}"
        