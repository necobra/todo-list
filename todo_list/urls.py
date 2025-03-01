from django.urls import path

from todo_list import views

urlpatterns = [
    path("",
         views.TaskListView.as_view(),
         name="task-list"),
    path("task/create/",
         views.TaskCreateView.as_view(),
         name="task-create"),
    path("task/<int:pk>/update/",
         views.TaskUpdateView.as_view(),
         name="task-update"),
    path("task/<int:pk>/delete/",
         views.TaskDeleteView.as_view(),
         name="task-delete"),
    path("task/<int:pk>/change_status/",
         views.change_task_done_status,
         name="task-change-status"),

    path("tags",
         views.TagListView.as_view(),
         name="tag-list"),
    path("tag/create/",
         views.TagCreateView.as_view(),
         name="tag-create"),
    path("tag/<int:pk>/update/",
         views.TagUpdateView.as_view(),
         name="tag-update"),
    path("tag/<int:pk>/delete/",
         views.TagDeleteView.as_view(),
         name="tag-delete"),

]
app_name = "todo_list"
