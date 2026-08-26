from django import forms
from .models import todo

class TodoForms(forms.ModelForm):
    class Meta:
        model= todo
        fields= ['todo', 'todo_dis']

        labels={
            'todo':'Todo Name',
            'todo_dis':'Todo Discription'
        }