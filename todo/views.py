from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.forms import ModelForm


class AddTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "summary", "completed"]


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html", {"todos": todos})


def add_todo(request):
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/add.html", {"form": form})
    return render(request, "todo/add.html", {"form": AddTodoForm()})


def update_todo(request, id):
    returned_todo = get_object_or_404(Todo, id=id)
    todoForm = AddTodoForm(request.POST or None, instance=returned_todo)
    if request.method == "POST":
        if todoForm.is_valid():
            todoForm.save()
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/update.html", {"form": todoForm})
    return render(request, "todo/update.html", {"form": todoForm})


def delete_todo(request, id):
    return_todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        return_todo.delete()
        return HttpResponseRedirect(reverse("todo:index"))
    return render(request, "todo/delete.html")
