from django.db import models
from django.utils import timezone 


# Create your models here.

class Task(models.Model): 
    task = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=timezone.now)
    complete = models.BooleanField(default = False)
   
    def __str__(self):
        return  f'{self.task}'
   