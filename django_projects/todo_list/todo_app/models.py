from turtle import title
from django.db import models

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=120, default='')
    description= models.TextField(default='')
    completed= models.BooleanField(default=False)

    def __str__(self):
        return self.title
