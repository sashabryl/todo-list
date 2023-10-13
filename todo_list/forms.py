from django import forms

from todo_list.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags",
        )
