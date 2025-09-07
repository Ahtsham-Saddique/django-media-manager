from django.db import models

# Create your models here.
class Media(models.Model):
    File_Name=models.CharField(max_length=100)
    Upload_File=models.FileField()

