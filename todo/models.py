from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    summary = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class User(models.Model):
    name = models.CharField(max_length=20)
    todos = models.ManyToManyField(Todo, blank=True, related_name="todos")

    def __str__(self):
        return f"{self.name}"

