from django.db import models

# Create your models here.
class Student(models.Model):
    # primary key shoud not be done that way as this will restrict change of roll_no in edit
    roll_no =  models.IntegerField(primary_key=True)
    name    =  models.CharField(max_length=120)
    cls   =   models.CharField(max_length=12)
    mobile  =  models.CharField(max_length=10)
    address =   models.CharField(max_length=400)
    
    def __str__(self):
        return str(self.roll_no)

class StudentAcademics(models.Model):
    student     = models.ForeignKey(Student,on_delete=models.CASCADE)
    math        = models.IntegerField(null=True,blank=True)
    physics     = models.IntegerField(null=True,blank=True)
    bio         = models.IntegerField(null=True,blank=True)
    chemistry   = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.student)