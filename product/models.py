from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class STAFF(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
  
    def __str__(self):
        return self.name
    
class Whse_Mangament(models.Model):
    name = models.CharField(max_length=200, null=True)        
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class TASKS(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Done', 'Done'),
            ('canceled', 'canceled'),
            )

    STAFF = models.ForeignKey(STAFF, null=True, on_delete=models.SET_NULL)
    Whse_Mangament = models.ForeignKey(Whse_Mangament,null=True, on_delete=models.SET_NULL)
    Descreption = models.CharField(max_length=1000,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    TASK_NO = models.CharField(max_length=1000,null=True)
    my_file=models.FileField(upload_to='',blank=True)
    
    
    
    def __str__(self):
		   return self.Whse_Mangament.name
           

class FULFILLED(models.Model):
    STATUS = (
            
            ('done', 'done'),
            ('didnot finish', 'didnot dinish'),
            
            )
    STAFF = models.ForeignKey(STAFF, null=True, on_delete=models.SET_NULL)
    Whse_Mangament = models.ForeignKey(Whse_Mangament,null=True, on_delete=models.SET_NULL)
    TASK_NO = models.CharField(max_length=1000, null=True)
    Descreption = models.CharField(max_length=1000,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, default="")
    



    def __str__(self):
    
		   return self.STAFF.name






    

    

    
   
          
