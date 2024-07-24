from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list import models
from todo_list import forms


class TaskListView(generic.ListView):
    model = models.Task
    queryset = (models.Task.objects
                .prefetch_related("tags")
                .order_by("-datetime"))


class TaskCreateView(generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm

    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm

    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = models.Task
    template_name = "todo_list/task_delete_confirm.html"
    success_url = reverse_lazy("todo_list:task-list")


def change_task_done_status(request, pk: int) -> HttpResponse:
    task = models.Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("/")


class TagListView(generic.ListView):
    model = models.Tag


class TagCreateView(generic.CreateView):
    model = models.Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = models.Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = models.Tag
    template_name = "todo_list/tag_delete_confirm.html"
    success_url = reverse_lazy("todo_list:tag-list")
