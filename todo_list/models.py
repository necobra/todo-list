from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["-datetime"]

    def __str__(self) -> str:
        return f"{self.content[:255]}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
