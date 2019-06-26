from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    writer = models.EmailField(widget=forms.EmailInput({'placeholder': 'test@example.com'}))
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

