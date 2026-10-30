from django import forms
from django.forms import widgets
from .models import STATUS_CHOICES

class TaskForm(forms.Form):
    description = forms.CharField(max_length=3000, widget=widgets.Textarea, required=True, label="Описание")
    detail_descriptions = forms.CharField(max_length=3000, widget=widgets.Textarea, required=False,
                                          label="Детальное описание")
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Статус")
    due_date = forms.DateField(required=False, widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
                               label="Дата выполнения")
