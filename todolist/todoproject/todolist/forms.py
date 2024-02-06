from django import forms

class TaskForm(forms.Form):
    new_task = forms.CharField(max_length=200, label='New Task')