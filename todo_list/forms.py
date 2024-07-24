from django import forms
from django.utils import timezone

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline_datetime = forms.DateTimeField(
        widget=forms.SelectDateWidget,
        required=False,
        label="Deadline"
    )

    class Meta:
        model = Task
        fields = ["content", "deadline_datetime", "tags"]

    def clean_deadline_datetime(self):
        deadline_datetime = self.cleaned_data.get("deadline_datetime")
        if deadline_datetime:
            if deadline_datetime < timezone.now():
                raise forms.ValidationError("Deadline cannot be in the past")
