from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeID= models.IntegerField()
    employeeName= models.CharField(max_length=60)
    employeeClass= models.CharField(max_length=20)
    employeeSection= models.CharField(max_length=20)
    employeeCity= models.CharField(max_length=20, default='NA')

    def __str__(self):
        return str(self.employeeID) + self.employeeName