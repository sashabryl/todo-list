from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    template_name = "task_list.html"
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
    template_name = "confirm_delete.html"


def complete_undo_task(request: HttpRequest, pk: int):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "confirm_delete.html"
