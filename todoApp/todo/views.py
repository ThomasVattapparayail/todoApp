from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import todo
from .forms import TodoForms

# Create your views here.

def index(request):
    if request.method == "POST":
        form = TodoForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TodoForms()

    data = {
        "form": form,
        "form_data": todo.objects.all()
    }

    return render(request, "index.html", data)

def edit(request, id):
    todo_data = get_object_or_404(todo, id=id)

    if request.method == "POST":
        form = TodoForms(request.POST, instance=todo_data)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TodoForms(instance=todo_data)

    return render(request, "edit.html", {"form": form})

def delete(request, id):
    todo_data = get_object_or_404(todo, id=id)

    if request.method == "POST":
        todo_data.delete()
        return redirect("index")

    return redirect("index")

def done(request, id):
    todo_data = get_object_or_404(todo, id=id)

    if request.method == "POST":
        todo_data.done = 1
        todo_data.save()
        return redirect("index")

    return redirect("index")