from django.db import models

# Create your models here.
class Upload(models.Model):
    file_name=models.CharField(max_length=100)
    upload_file=models.FileField() 

    def __str__(self):
        return self.file_name