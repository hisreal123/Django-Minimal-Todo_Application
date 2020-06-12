from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model): 
    task = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now=timezone.now)
    complete = models.BooleanField(default = False)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)
   
    def __str__(self):
        return  f'{self.author} created {self.task}'
   