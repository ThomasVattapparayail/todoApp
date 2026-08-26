from django.db import models

# Create your models here.

class todo(models.Model):
    todo=models.CharField(max_length=255)
    todo_dis=models.TextField()
    todo_date=models.DateField(auto_now=True)
    done=models.IntegerField(default=0)

    def __str__(self):
        return self.todo
