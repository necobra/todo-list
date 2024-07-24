from django.contrib import admin

from todo_list import models


admin.register(models.Tag)
admin.register(models.Task)
