from django.db import models

# Create your models here.
class ClassTable(models.Model):
    class_name=models.CharField(max_length=255)
    
class StudentTable(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    date_of_birth=models.DateField()
    class_name=models.ForeignKey(ClassTable,on_delete=models.CASCADE)
    guardian_Contact=models.CharField(max_length=255)
    