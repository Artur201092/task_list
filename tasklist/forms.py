from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)


