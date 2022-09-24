from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_todo, name="add"),
    path("<int:id>/update", views.update_todo, name="update"),
    path("<int:id>/delete", views.delete_todo, name="delete"),
    path("<int:id>/detail", views.detail_todo, name="detail"),
]

