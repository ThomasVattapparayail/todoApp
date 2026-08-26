from django.db import models

# Create your models here.

class todo(models.Model):
    todo=models.CharField(max_length=255)
    todo_dis=models.TextField()
    todo_date=models.DateField(auto_now=True)
