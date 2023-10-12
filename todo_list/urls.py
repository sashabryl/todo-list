from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskDeleteView,
    TaskCreateView,
    TaskUpdateView,
    complete_undo_task,
    TagUpdateView,
    TagCreateView,
    TagDeleteView,
    TagListView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "<int:pk>/task-update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),

    path(
        "<int:pk>/task-delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "<int:pk>/complete-undo/",
        complete_undo_task,
        name="task-complete-undo",
    ),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("<int:pk>/tag-update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
    path("<int:pk>/tag-delete/", TagDeleteView.as_view(), name="tag-delete"),
]


app_name = "todo"
