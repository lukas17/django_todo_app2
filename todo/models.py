from django.db import models
from django import forms 

class Todo(models.Model):
    text = models.CharField(max_length=40)
    writer = models.EmailField(max_length=255,default='you default value or example@email.com')
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

